# 🚀 Smart Motion Detection Surveillance System (Python + OpenCV)

A real-time motion detection system using Python and OpenCV that detects movement from a webcam, classifies motion intensity, and automatically saves snapshots and videos when significant motion is detected.


## Features

### 🧠 Core Features
- Real-time motion detection using webcam
- Frame differencing technique using OpenCV
- Bounding boxes around moving objects
- Noise filtering to ignore small movements

### 📸 Smart Capture System
- Automatically saves snapshots when motion is detected
- Timestamp-based file naming
- Organized folder structure for images and videos

### 🎥 Intelligent Video Recording
- Records video only when Medium or High motion is detected
- 10-second automatic recording
- Saves videos with timestamped filenames

### 📊 Motion Analysis
- Detects motion intensity levels:
  - 🟢 Low
  - 🟡 Medium
  - 🔴 High
- Displays intensity on live video feed

### ⏱ Smart Cooldown System
- Prevents repeated triggers using a 10-second cooldown timer


## 🧰 Tech Stack

- Python 3.x
- OpenCV
- datetime (built-in)
- os (built-in)
- time (built-in)


## 📁 Project Structure
motion-detection-system/
│
├── motion_detector.py
├── motion_images/
│ ├── snapshot_2026-04-25_12-00-01.jpg
│
├── motion_videos/
│ ├── video_2026-04-25_12-00-01.avi
│
└── README.md


## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/motion-detection-system.git
cd motion-detection-system