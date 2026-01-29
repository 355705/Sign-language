# 🗣️ Smart Sign Language Translator (AI-Powered)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow)

## 📌 Project Overview
This project is a real-time **Sign Language to Text & Speech Translator**. It uses computer vision and machine learning to recognize hand gestures and translate them into spoken language instantly.

The system is designed to bridge the communication gap for the hearing-impaired community, offering a seamless interface that detects both **single-hand** and **two-hand** gestures using a hybrid data processing approach.

## 🧠 Hybrid Gesture Recognition
The system dynamically detects whether one or two hands are present.
- Single hand → landmarks padded automatically
- Two hands → full landmark vector used
This ensures a fixed-size feature vector for the classifier.

## 🚀 Features
- **Real-Time Detection:** Uses MediaPipe for ultra-fast hand landmark extraction.
- **Hybrid Recognition:** Supports both single-hand gestures (e.g., "Hello") and two-hand gestures (e.g., "Help") using dynamic padding.
- **Text-to-Speech (TTS):** Converts recognized gestures into audio feedback using `pyttsx3`.
- **Interactive GUI:** A professional interface built with **Tkinter** displaying the camera feed, prediction text, and control buttons.
- **Custom Dataset:** The model is trained on a custom-built dataset of 13 different sentences/commands.

## ⚠️ Limitations
- Requires a clean background for best accuracy.
- Currently supports a limited set of predefined gestures.

## 🛠️ Tech Stack
- **Language:** Python 3.10
- **Computer Vision:** OpenCV, MediaPipe
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **GUI:** Tkinter, Pillow
- **Audio:** pyttsx3

## 📂 Project Structure

```text
├── data/                     # Dataset images (Class 0 to 12).
├── model.p                   # Trained model file.
├── data.pickle               # Preprocessed landmarks data.
├── create_imgs.py            # Script to capture dataset via webcam.
├── create_dataset.py         # Script to convert images to landmarks.
├── train_classifier.py       # Script to train the Random Forest model.
├── GUI.py                    # Main Application (GUI + Prediction).
├── requirements.txt          # List of dependencies.
└── README.md                 # Project documentation.
 ```
## ⚙️ Installation

1. **Create a Virtual Environment (Recommended):**
```bash
python -m venv venv
```
- **Windows:**
```bash
.\venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

2. **Install Dependencies:** **📝 Note:** Specific versions are required to avoid protocol buffer conflicts.
```bash
pip install -r requirements.txt
```

## 🧠 How to Train Your Own Model
If you want to add new gestures or retrain the model, follow these steps:

#### *Step 1: Collect Data*
Run the collection script to capture images for your classes (0-12).
```bash
python create_imgs.py
```
- 📌 Press **S** to capture images for each class.

#### *Step 2: Preprocess Data*
Convert images into normalized hand landmarks (Points). This script handles padding to support both single and dual hands.
```bash
python create_dataset.py
```
#### *Step 3: Train Classifier*
Train the Random Forest model.
```bash
python train_classifier.py
```
- 📌 Training Accuracy may reach up to 100% on the training set.
For better generalization, increasing dataset size is recommended.

## 🎮 How to Run the App
To start the main translation interface:
```bash
python GUI.py
```
#### Controls:

Sign: Perform a gesture in front of the camera.

Speak: Click the "🔊 SPEAK" button to hear the translation. **📝 Note:** I remove it in final edition but code still in GUI.py

Exit: Click "❌ EXIT" to close the application.

## 🔍 Supported Gestures (Classes) 
```text
The current model is trained on the following 13 Arabic sign classes:
0: ' اهلا', 1: 'حبيبي', 2: 'شكرًا', 3: 'أسف',
4: 'انا مبسوط', 5: 'أب', 6: 'أم', 7: 'أخ',
8: 'مريض', 9: 'ساعدنى', 10: 'أوعدك', 11: 'صاحب', 12: 'مستشفى'
```

## 🐛 Troubleshooting
**Issue:**
AttributeError: module 'mediapipe' has no attribute 'solutions' Fix: This is caused by a version conflict between MediaPipe and Protobuf. Ensure you use the versions specified in requirements.txt:
```bash
pip install mediapipe==0.10.9 protobuf==3.20.3
```

## 🎥 References & Acknowledgements
This project was inspired by tutorial from Computer Vision Engineer. Check out the video here:

[Sign language detection with Python and Scikit Learn](https://youtu.be/MJCSjXepaAM?si=qfpahnFkr0j1fx7v)

## 👨‍💻 Author
**Mohamed Adel**  
AI & Computer Vision Enthusiast  

- GitHub: https://github.com/355705  
- LinkedIn: https://linkedin.com/in/mohamed-adel01
