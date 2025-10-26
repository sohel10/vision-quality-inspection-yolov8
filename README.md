# 🚗 License Plate Recognition (YOLOv8 + EasyOCR)

## 📌 Overview
This project implements an end-to-end Automatic License Plate Recognition (ALPR) pipeline.

The system:
- Detects license plates in images and videos using YOLOv8 (object detection)
- Extracts the text on the plate using EasyOCR (optical character recognition)
- Outputs both visual evidence (annotated frames, cropped plates) and structured data (CSV logs)

This pattern is common in fleet analytics, gate access control, tolling, parking enforcement, and traffic safety.

## 🔍 What the pipeline does
- 🔎 Detects plates frame-by-frame
- 🧠 Reads plate characters (e.g. "ABC1234")
- 🗂 Logs each detection with timestamp, bounding box, and confidence score
- 🖼 Saves:
  - Annotated images/video with boxes + labels
  - Cropped plate images
  - A CSV audit trail of all detections

## 🧰 Tech Stack
- **YOLOv8 (Ultralytics)** – real-time license plate detection
- **EasyOCR** – OCR for plate text extraction
- **OpenCV** – image/video processing
- **Pandas** – structured logging and analytics
- **Python 3.9** – packaged to run in a conda environment


---

## 📂 Project Structure
├── lpr_image.py # Main detection + OCR script
├── lpr_utils.py # Helper functions
├── train.py # YOLO training script
├── assets/
│ ├── inputs/ # Sample images/videos
│ └── outputs/ # Results (vis, crops, preds.csv)
├── requirements.txt # Dependencies
└── README.md
##2. Create & activate conda environment
conda create -n lpr python=3.9 -y
conda activate lpr
## 3. Install dependencies
pip install -r requirements.txt
## 4 Run on a single image
python lpr_image.py --source assets/inputs/car.jpg --weights runs/detect/train8/weights/best.pt --device cpu
## 5 Run on a video
python lpr_image.py --source assets/inputs/car.mp4 --weights runs/detect/train8/weights/best.pt --device cpu
#  Outputs

Annotated frames/video → assets/outputs/vis/

Cropped license plates → assets/outputs/crops/

Detection + OCR CSV → assets/outputs/preds.csv
## Roadmap

 Image support

 Video support

 CSV logging

 Live webcam support (--source 0)

 Streamlit deployment for interactive UI
## License

For educational and research purposes

## Acknowledge Ultralytics YOLOv8
 and EasyOCR 
 
