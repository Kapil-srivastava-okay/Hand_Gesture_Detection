# Hand Gesture Detection using TensorFlow

## Description
This project consists of two main components:
1. **ForImageCollection.ipynb** - A script for collecting hand gesture images for training a deep learning model.
2. **HandGestureDetect.ipynb** - A notebook that trains a TensorFlow object detection model to recognize hand gestures.

## Features
- Collects images for hand gesture recognition.
- Uses TensorFlow's Object Detection API.
- Implements model training using SSD MobileNet v2.
- Converts the trained model to TensorFlow Lite (TFLite) for deployment.
- Evaluates model performance using mAP (mean Average Precision).
- ![My Image](https://raw.githubusercontent.com/Kapil-srivastava-okay/Hand_Gesture_Detection/workspace/images/extra/Screenshot 2025-02-14 150211.png)

## Installation & Requirements
Ensure you have the following installed:
- Python 3.7+
- OpenCV
- TensorFlow 2.x
- NumPy
- Google Colab (optional, but recommended)

To install dependencies, run:
```bash
pip install opencv-python tensorflow numpy
```
## Usage
1. **Image Collection** - Run ForImageCollection.ipynb to collect images for different hand gestures. The script:
- Uses OpenCV to capture images from a webcam.
- Saves images into labeled directories.
  
2. **Model Training** - Run HandGestureDetect.ipynb to:
- Prepare the dataset and create TFRecords.
- Choose and configure the SSD MobileNet v2 model.
- Train the model on the collected dataset.
- Convert the trained model to TFLite for efficient deployment.
  
3. **Testing the Model**
- The model is evaluated on a test dataset.
- Performance is measured using mean Average Precision (mAP).
- The trained model is exported as detect.tflite.
  
## Results
- The model detects hand gestures accurately after training.
- The TFLite model is ready for deployment on mobile or edge devices.
  
## Contributors
- Kapil Srivastava 
  
## License
This project is licensed under the MIT License. Feel free to modify and use it.
