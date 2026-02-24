# 🧍 Real-Time Person Detection using YOLO

This project performs real-time person detection using YOLO (Ultralytics) and OpenCV.  
It captures video from your webcam and detects only the "person" class with a confidence threshold.

---

## 🚀 Features

- Real-time webcam detection
- Detects only **person** class
- Displays live person count
- Confidence threshold control
- Clean and lightweight implementation

---

## 🛠️ Tech Stack

- Python
- OpenCV
- Ultralytics YOLO

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/person-detection-yolo.git
cd person-detection-yolo
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python imagedetect.py
```

Press **Q** to quit the webcam window.

---

## 📂 Project Structure

```
person-detection-yolo/
│
├── imagedetect.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Model Used

This project uses the lightweight YOLO model:

```
yolo11n.pt
```

If not downloaded automatically, get it from the official Ultralytics documentation.

---

## 📸 Output

- Bounding boxes around detected persons
- Live person count displayed on screen

---

## 🎯 Future Improvements

- Add video file input support
- Add GUI interface
- Convert into Flask/FastAPI API
- Deploy as web application

---

## 👩‍💻 Author

Your Name  
GitHub: https://github.com/yourusername
