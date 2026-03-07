from ultralytics import YOLO

model = YOLO("runs/detect/train14/weights/best.pt")

results = model("test/images")

for r in results:
    r.show()