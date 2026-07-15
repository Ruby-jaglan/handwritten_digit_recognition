**NAME:-** Ruby Jaglan               **CODTECH INTERN ID:-** CITS4103
# ✍️ Handwritten Digit Recognition Using Deep Learning

## 📌 Project Overview

Handwritten Digit Recognition is a Deep Learning web application that identifies handwritten digits (0–9) from uploaded images. The project uses the MNIST dataset to train a neural network model capable of recognizing handwritten digits with high accuracy. A Flask-based web interface allows users to upload an image and instantly receive the predicted digit along with the model's confidence score.

---

## 🎯 Objective

The objective of this project is to build an intelligent system that can recognize handwritten digits using Deep Learning. It demonstrates the complete workflow of image preprocessing, model training, prediction, and deployment using a Flask web application.

---

## 🚀 Features

- Recognizes handwritten digits (0–9)
- Built using Deep Learning (TensorFlow & Keras)
- Uses the MNIST handwritten digit dataset
- Upload image and predict the digit instantly
- Displays prediction confidence
- User-friendly Flask web interface
- Beginner-friendly and easy-to-understand code
- Suitable for academic projects and GitHub portfolios

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- Pillow (PIL)
- HTML
- CSS

---

## 📂 Project Structure

```
Handwritten-Digit-Recognition/
│
├── dataset/
├── models/
│   └── handwritten_digit_model.keras
│
├── notebook/
│   └── handwritten_digit_recognition.ipynb
│
├── static/
│   ├── uploads/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Project Workflow

1. Load the MNIST dataset.
2. Preprocess and normalize image data.
3. Build a Deep Learning model using TensorFlow/Keras.
4. Train the model on handwritten digit images.
5. Save the trained model.
6. Upload a handwritten digit image through the Flask web app.
7. Predict the digit and display the confidence score.

---

## 📁 Dataset

This project uses the **MNIST Handwritten Digit Dataset**, which is automatically downloaded through TensorFlow during model training.

- 60,000 Training Images
- 10,000 Testing Images
- 28 × 28 Grayscale Images
- Digits from 0 to 9

---

## 🧠 Deep Learning Model

The model is built using TensorFlow/Keras with the following layers:

- Flatten Layer
- Dense Layer (128 neurons, ReLU)
- Dense Layer (64 neurons, ReLU)
- Output Layer (10 neurons, Softmax)

Optimizer:
- Adam

Loss Function:
- Categorical Crossentropy

Evaluation Metric:
- Accuracy

---

### Navigate to the project folder

```bash
cd Handwritten-Digit-Recognition
```

### Train the model

```bash
python train_model.py
```

### Run the Flask application

```bash
python app.py
```

## 📸 Application Workflow

1. Open the web application.
2. Upload a handwritten digit image.
3. Click the **Predict Digit** button.
4. The model processes the image.
5. The predicted digit and confidence score are displayed.

---

## 💡 Future Enhancements

- Draw digits directly on a canvas
- Drag-and-drop image upload
- Real-time prediction
- Confidence visualization with charts
- Support for custom handwritten datasets
- Mobile-responsive UI
- Cloud deployment (Render, Railway, or Azure)

---

## 🎓 Learning Outcomes

This project demonstrates:

- Deep Learning Fundamentals
- Image Classification
- Neural Networks
- TensorFlow & Keras
- Image Preprocessing
- Flask Web Development
- Model Deployment
- Git & GitHub Version Control

---

