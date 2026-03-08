from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import numpy as np
import cv2
import time
from pathlib import Path
from ultralytics import YOLO
import logging
from prometheus_fastapi_instrumentator import Instrumentator

# =========================
# App
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Object Detection API",
    version="1.0.0"
)

app.state.build_id = str(int(time.time()))

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# =========================
# Monitoring
# =========================

Instrumentator().instrument(app).expose(app)

# =========================
# Config
# =========================

MODEL_PATH = Path("models/best.pt")

model = None

# =========================
# Startup
# =========================

@app.on_event("startup")
def load_model():
    global model

    if not MODEL_PATH.exists():
        raise RuntimeError("Model file not found")

    model = YOLO(str(MODEL_PATH))

    logger.info("YOLO model loaded")

# =========================
# Health Check
# =========================

@app.get("/health")
def health():
    return {"status": "healthy"}

# =========================
# Detection Endpoint
# =========================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    logger.info("Prediction request received")

    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type")

    contents = await file.read()

    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    results = model(img)

    detections = []

    for box in results[0].boxes:
        detections.append({
            "x1": float(box.xyxy[0][0]),
            "y1": float(box.xyxy[0][1]),
            "x2": float(box.xyxy[0][2]),
            "y2": float(box.xyxy[0][3]),
            "confidence": float(box.conf),
            "class": int(box.cls)
        })

    logger.info(f"Detections found: {len(detections)}")

    return {
        "detections": detections,
        "count": len(detections)
    }
# =========================
# Web UI
# =========================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "build_id": app.state.build_id
        }
    )

