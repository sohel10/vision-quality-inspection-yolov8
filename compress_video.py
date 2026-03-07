import cv2
import os

input_video = "runs/detect/predict/car_1.avi"
output_video = "runs/detect/predict/car_demo.mp4"

# check if file exists
if not os.path.exists(input_video):
    print("Error: Input video not found:", input_video)
    exit()

cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

# sometimes fps returns 0
if fps == 0:
    fps = 25

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Original Resolution:", width, "x", height)
print("FPS:", fps)

# reduce resolution
new_width = 640
scale = new_width / width
new_height = int(height * scale)

print("New Resolution:", new_width, "x", new_height)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video, fourcc, fps, (new_width, new_height))

frame_count = 0
max_frames = int(fps * 8)  # keep 8 seconds

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (new_width, new_height))

    out.write(frame)

    frame_count += 1

    if frame_count >= max_frames:
        break

cap.release()
out.release()

print("Compressed video saved:", output_video)
print("Total frames written:", frame_count)