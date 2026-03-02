
Object dog poo health  - v3 2021-10-07 10:54pm
==============================

This dataset was exported via roboflow.com on March 1, 2026 at 8:29 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 140 images.
Hge-vs-healthy-dog-poo are annotated in YOLO26 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Random rotation of between -32 and +32 degrees

The following transformations were applied to the bounding boxes of each image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Randomly crop between 0 and 35 percent of the bounding box
* Random shear of between -15° to +15° horizontally and -23° to +23° vertically
* Random brigthness adjustment of between -24 and +24 percent


