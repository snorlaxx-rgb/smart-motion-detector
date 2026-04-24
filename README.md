# 📸 Smart Motion Detection System

A real-time motion detection system built using Python and OpenCV.  
It works like a basic CCTV camera that detects movement using webcam input.


## 🚀 Features
- Real-time motion detection using webcam
- Detects moving objects using frame difference technique
- Draws bounding boxes around motion areas
- Noise reduction using grayscale and blur processing


## 🧠 How it works
The system captures two consecutive frames from the webcam, compares them to find differences, processes the image to remove noise, and detects regions where movement occurs.


## 🛠️ Tech Stack
- Python
- OpenCV
- NumPy


## ▶️ How to run
1. Install dependencies:
```bash
pip install opencv-python numpy