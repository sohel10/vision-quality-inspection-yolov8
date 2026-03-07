from ultralytics import YOLO
import mlflow


def main():

    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("yolo_license_plate")

    with mlflow.start_run():

        model = YOLO("yolov8s.pt")

        epochs = 30
        img_size = 640

        results = model.train(
            data="data.yaml",
            epochs=epochs,
            imgsz=img_size,
            device="cuda"
        )

        mlflow.log_param("epochs", epochs)
        mlflow.log_param("img_size", img_size)


if __name__ == "__main__":
    main()