SmartYardScan – Dog Waste Detection

Tyler Boda

Tier 2 – Custom Object Detection


Problem Statement:

Dog waste is often left on lawns and sidewalks, creating hygiene and cleanliness issues. Manually identifying and documenting it takes time and effort. This project aims to automatically detect and count dog waste in images.

Solution Overview:

The system takes an image as input and uses a YOLOv8 object detection model to locate dog waste. It outputs an annotated image with bounding boxes and a total count of detected objects.

## Results (Initial Training)

Model: YOLOv8n  
Epochs: 25  
Image Size: 640  
Device: CPU  

Validation Results:
- Precision: 0.994
- Recall: 1.000
- mAP50: 0.995
- mAP50-95: 0.995

## Demo Output
Sample predictions are saved in:
runs/detect/predict/