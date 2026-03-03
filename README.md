# SmartYardScan – Automated Dog Waste Detection
Tyler Boda  
ITAI 1378 – Midterm Project  
Tier 2 – Custom Object Detection  

---

## Project Overview

SmartYardScan is a computer vision system that detects and counts dog waste in images using object detection. The goal is to automate visual inspection for residential neighborhoods, HOAs, and pet waste service providers.

---

## Tier Selection

Tier 2 – Custom Object Detection

This project involves training a YOLOv8 model on a custom dataset to detect a specific real-world object (dog waste). The model was fine-tuned on labeled images and evaluated using standard object detection metrics.

---

## Problem Statement

Dog waste is frequently left on lawns and sidewalks, creating hygiene, sanitation, and aesthetic issues. Manual inspection of medium-sized neighborhoods can take 1–2 hours per walkthrough and may lead to inconsistent reporting.

Stakeholders:
- Homeowners
- HOAs
- Property managers
- Pet waste removal services

Automating detection can reduce inspection time and support better reporting and routing decisions.

---

## Solution Overview

The system uses YOLOv8 object detection to automatically identify dog waste in images.

Pipeline:

Input Image → Resize / Preprocess → YOLOv8 Inference → Bounding Box Detection → Object Count Output

The output includes:
- Annotated image with bounding box
- Confidence score
- Total object count

---

## Technical Approach

Technique: Object Detection  
Model: YOLOv8n (Ultralytics)  
Framework: PyTorch (Ultralytics implementation)

Justification:
YOLOv8n was selected because it provides strong detection performance while remaining lightweight and efficient. It is suitable for near real-time inference on CPU hardware.

Training Configuration:
- Image size: 640x640
- Epochs: 25
- Device: CPU (Intel i5)
- Pretrained weights: yolov8n.pt

---

## Dataset Plan

Source:
Roboflow Universe – Dog Poo Health Dataset (MIT License)

Dataset Size:
- 126 training images
- 8 validation images

Classes:
Original dataset contained multiple classes. All labels were merged into a single class:
- dog_poop

Preparation Steps:
- Converted multi-class labels to single class
- Verified YOLO format labels
- Cleaned and corrected data.yaml configuration

Limitation:
The dataset is relatively small, which may limit generalization to unseen environments.

---

## Metrics

Primary Metric:
Target mAP50 ≥ 0.70  
Achieved mAP50: 0.995  

Secondary Metrics:
Precision: 0.994  
Recall: 1.000  
mAP50-95: 0.995  
Inference Speed: ~0.18 seconds per image (CPU)

Interpretation:
High recall indicates all validation objects were detected.  
High precision indicates minimal false positives.  
Due to small validation size (8 images), further testing on unseen data is recommended.

---

## Week-by-Week Plan

| Week | Task |
|------|------|
| 10 | Dataset acquisition + environment setup |
| 11 | Initial training + debugging |
| 12 | Model tuning + label verification |
| 13 | Demo generation + testing |
| 14 | Documentation + slide preparation |
| 15 | Presentation |

---

## Risks & Mitigation

| Risk | Probability | Mitigation |
|------|------------|------------|
| Small dataset size | Medium | Collect additional real-world images |
| Overfitting | Medium | Data augmentation + more validation images |
| False positives (rocks, leaves) | Medium | Add negative "no-poop" images |
| CPU training speed | Low | Use lightweight YOLOv8n model |

---

## Resources Needed

Compute:
- Local CPU (Intel i5)

Frameworks:
- Ultralytics YOLO
- PyTorch

Cost:
- $0

Data:
- Roboflow (MIT license dataset)

---

## AI Usage Log

ChatGPT was used for:
- Structuring the project proposal
- Debugging environment and Git setup
- Reviewing slide clarity and formatting
- README organization guidance

All model training, evaluation, and testing were performed locally.