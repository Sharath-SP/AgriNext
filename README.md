# 🌱 AgriNext: An AI-Based Smart Farming System

AgriNext is an AI-powered smart farming application designed to support farmers in making better agricultural decisions. The system combines machine learning and deep learning techniques to provide **crop recommendations** based on soil and environmental conditions and **plant disease identification** from leaf images.

---

## 📌 Overview

Agriculture depends heavily on factors such as soil nutrients, temperature, humidity, rainfall, and plant health.

AgriNext addresses these challenges through two major AI-powered modules:

1. **Crop Recommendation** – recommends a suitable crop based on soil and environmental parameters.
2. **Plant Disease Identification** – identifies plant diseases from uploaded leaf images using a CNN-based deep learning model.

The application provides these capabilities through a user-friendly web interface.

---

## ✨ Key Features

### 🌾 Crop Recommendation

The system recommends suitable crops using:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Seven classification algorithms were evaluated for the crop recommendation task:

- Decision Tree
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest
- XGBoost
- K-Nearest Neighbors (KNN)

The existing project evaluation reports **Random Forest as the best-performing model**, with an accuracy of approximately 99.55%.

### 🍃 Plant Disease Identification

The plant disease module uses a **Convolutional Neural Network (CNN)** to classify diseases from plant leaf images.

The model is trained for **38 disease classes across multiple crops**, including:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Bell Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

The model can identify both healthy plants and specific diseases within its supported classes.

---

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Application | Streamlit |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow / Keras |
| Data Processing | Pandas, NumPy |
| Image Processing | PIL / OpenCV |
| Machine Learning Model | Random Forest |
| Deep Learning Model | CNN |
| Version Control | Git & GitHub |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      AgriNext       │
                    │    Web Application  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐           ┌──────────────────┐
       │ Crop            │           │ Plant Disease    │
       │ Recommendation  │           │ Identification   │
       └────────┬────────┘           └─────────┬────────┘
                │                              │
                ▼                              ▼
       Soil & Environmental             Plant Leaf Image
            Parameters                       │
                │                            │
                ▼                            ▼
       Machine Learning Model             CNN Model
                │                            │
                ▼                            ▼
        Recommended Crop              Disease Prediction