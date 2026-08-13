# 🌱 AgriNext — AI-Based Smart Farming System

AgriNext is an AI-powered smart farming system designed to assist farmers with data-driven agricultural decisions.

The system integrates **Machine Learning** and **Deep Learning** to provide:

- 🌾 Crop recommendations based on soil and environmental parameters
- 🍃 Plant disease identification from leaf images

The project combines a web-based frontend with independently deployed Streamlit AI modules.

---

## 🚀 Live Demo

### 🌾 Crop Recommendation
https://agrinext-crop-recommendation.streamlit.app/

### 🍃 Plant Disease Identification
https://agrinext-plant-disease.streamlit.app/

---

## 🎯 Project Overview

Agricultural decisions depend on multiple factors such as soil nutrients, temperature, humidity, rainfall, soil pH, and plant health.

AgriNext addresses these challenges through two AI-powered modules.

### 1. 🌾 Crop Recommendation

The Crop Recommendation module predicts a suitable crop using:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Several classification algorithms were evaluated during development:

- Decision Tree
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest
- XGBoost
- K-Nearest Neighbors (KNN)

The final application uses a **Random Forest classifier** for crop prediction.

### 2. 🍃 Plant Disease Identification

The Plant Disease Identification module uses a **Convolutional Neural Network (CNN)** to classify plant leaf images.

The trained model supports **38 disease/healthy classes** across multiple crops, including:

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

Users can upload a leaf image and receive a predicted disease class through the Streamlit application.

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │       AgriNext Web      │
                         │        Interface        │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ▼                                   ▼
          ┌────────────────────┐             ┌──────────────────────┐
          │ Crop Recommendation│             │ Plant Disease        │
          │ Streamlit App      │             │ Identification App   │
          └──────────┬─────────┘             └──────────┬───────────┘
                     │                                  │
                     ▼                                  ▼
          Soil & Environmental                  Leaf Image Upload
               Parameters                              │
                     │                                  │
                     ▼                                  ▼
          Random Forest Model                    CNN Model
                     │                                  │
                     ▼                                  ▼
             Recommended Crop                    Disease Prediction