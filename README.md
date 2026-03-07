![CI-CD](https://github.com/sohel10/object-detection/actions/workflows/cicd.yml/badge.svg)


# 🚗 Production-style computer vision inference platform built using YOLOv8 object detection and Docker-based deployment with automated CI/CD pipelines and AWS cloud infrastructure.

# 🧰 Tech Stack

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red)](https://ultralytics.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blue)](https://opencv.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API%20Service-success)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-success)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)](https://aws.amazon.com/)

This pattern is common in fleet analytics, gate access control, tolling, parking enforcement, and traffic safety.

## 🔍 What the pipeline does
- 🔎 Detects plates frame-by-frame
- 🧠 Reads plate characters (e.g. "ABC1234")
- 🗂 Logs each detection with timestamp, bounding box, and confidence score
- 🖼 Saves:
  - Annotated images/video with boxes + labels
  - Cropped plate images
  - A CSV audit trail of all detections

## 📌 Overview
This project implements an end-to-end Automatic License Plate Recognition (ALPR) pipeline.

The system:
- Detects license plates in images and videos using YOLOv8 (object detection)
- Extracts the text on the plate using EasyOCR (optical character recognition)
- Outputs both visual evidence (annotated frames, cropped plates) and structured data (CSV logs)

The platform includes:

- Object detection inference API
- Containerized deployment
- CI/CD automation
- Cloud deployment on AWS
- Production ML system architecture

## Monitoring Dashboard

### Prometheus Metrics

![Prometheus Metrics](docs/figures/prometheus_metrics.png)

### Grafana Dashboard

![Grafana Dashboard](docs/figures/grafana_dashboard.png)

### API Demo

![API Demo](docs/figures/api_demo.png)


# 🏗 System Architecture

The ML inference workflow follows a typical **production ML architecture**.
```` text
Client Image / Video
│
▼
YOLOv8 Object Detection
│
▼
Bounding Box Prediction
│
▼
Structured Output (JSON)

````
# Production deployment architecture:

```` text
Developer Push Code
│
▼
GitHub Repository
│
▼
GitHub Actions CI/CD
│
▼
Docker Image Build
│
▼
AWS ECR Container Registry
│
▼
AWS EC2 Deployment
│
▼
FastAPI Inference API
│
▼
YOLOv8 Model Prediction
````
## Production Features

This platform includes several production-grade ML infrastructure components:

- Containerized ML inference service using Docker
- Automated CI/CD pipeline with GitHub Actions
- Cloud deployment using AWS (ECR + EC2)
- Prometheus metrics monitoring
- Grafana performance dashboards
- Structured logging for inference requests
- Load-balanced API deployment for scalable inference

## Monitoring

The system exposes runtime metrics using Prometheus.

Metrics include:

- HTTP request count
- API latency
- error rate
- service health

Metrics endpoint:

/metrics

Metrics are visualized using Grafana dashboards.

## Logging

The API implements structured logging for inference requests.

Logs capture:

- request timestamp
- prediction latency
- detection count
- error events

Logs help monitor model behavior and debug production issues.

## Scalable Deployment

The system supports horizontal scaling through load-balanced container deployment.

Architecture:

Client → Load Balancer → FastAPI containers → YOLO inference

This enables the system to handle large volumes of inference requests.

