# 🚨 Smart Motion Detection System (Python + OpenCV)

A real-time motion detection system built using Python and OpenCV.  
It detects movement using a webcam, draws bounding boxes around moving objects, and automatically saves snapshots when motion is detected.


## 📌 Features

- 🎥 Real-time motion detection using webcam
- 📦 Detects and highlights moving objects with bounding boxes
- 🔇 Filters small noise using contour area threshold
- 📸 Automatically saves snapshots when motion is detected
- 🕒 Timestamped images for tracking events
- 📁 Saves images in a separate folder (`motion_images`)
- 🧠 Uses frame difference-based motion detection


## 🛠️ Technologies Used

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- os module
- datetime module


## 🚀 How It Works

1. Captures video from webcam
2. Compares consecutive frames to detect changes
3. Converts difference to grayscale
4. Applies blur + thresholding to remove noise
5. Detects contours of moving objects
6. Draws bounding boxes around detected motion
7. Saves snapshot with timestamp when motion is detected



## ⚙️ Installation

### 1. Install dependencies
```bash
pip install opencv-python numpy