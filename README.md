# Face Recognition System
Face Recognition System This project implements a face recognition system using OpenCV and a Local Binary Patterns Histogram (LBPH) classifier. The system can detect faces in real-time using a webcam and match them against a pre-trained database.

<img width="911" alt="image" src="https://github.com/user-attachments/assets/8ed1175a-2cc1-4e4d-b117-de33c6383124">



#Face_recognition/
│                
├── Dataset creater.py             # Script to create a dataset of face images
├── dataset/                       # Directory containing captured face images
├── detect.py                      # Main script for face detection and recognition
├── haarcascade_frontalface_default.xml  # Pre-trained XML classifier for face detection
├── recognizer/                    # Directory containing local trained xml file
├── sqlite.db                      SQLite database for storing face data
└── trainer.py                     # Script to train the face recognition model


#Features
Face Detection: Detects faces using the Haar Cascade Classifier.
Face Recognition: Recognizes faces using the LBPH algorithm.
Dataset Creation: Captures face images from the webcam and stores them in a dataset.
Model Training: Trains the face recognition model using the captured dataset.

#Requirements
Python 3.x
OpenCV
NumPy
SQLite3
Setup

#How to Use it:
1.dataset creater.py: Use this script to capture face images from the webcam.
2.trainer.py: Trains the LBPH model on the captured dataset.
3.detect.py: Detects and recognizes faces in real-time using the webcam.
