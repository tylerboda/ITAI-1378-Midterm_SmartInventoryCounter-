from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("bus.jpg")  # uses the local file you already have

print("Detections:")
for box in results[0].boxes:
    cls = int(box.cls)
    conf = float(box.conf)
    print(results[0].names[cls], round(conf, 3))