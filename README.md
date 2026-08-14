# 🌱 AgriNext — AI-Based Smart Farming System

AgriNext is an AI-powered smart farming system designed to assist farmers in making data-driven agricultural decisions.

The project combines **Machine Learning, Deep Learning, and Streamlit** to provide two core AI-powered capabilities:

- 🌾 **Crop Recommendation** — recommends a suitable crop based on soil and environmental parameters.
- 🍃 **Plant Disease Identification** — identifies plant diseases from uploaded leaf images using a CNN-based deep learning model.

The two AI modules are independently deployed as Streamlit applications and are accessible through the AgriNext web interface.

---

## 🚀 Live Applications

| Module | Live Application |
|---|---|
| 🌾 Crop Recommendation | [Launch Crop Recommendation](https://agrinext-crop-recommendation.streamlit.app/) |
| 🍃 Plant Disease Identification | [Launch Plant Disease Identification](https://agrinext-plant-disease.streamlit.app/) |

---

## 🎯 Project Objectives

Agricultural decisions depend on several factors, including soil nutrients, temperature, humidity, rainfall, soil pH, and plant health.

AgriNext aims to provide farmers with AI-assisted tools that can help with:

- Selecting suitable crops based on environmental conditions
- Identifying diseases from plant leaf images
- Providing an accessible web-based interface for AI-powered agricultural assistance

---

## ✨ Key Features

### 🌾 Crop Recommendation

The system predicts a suitable crop using the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

During development, multiple machine learning algorithms were evaluated:

- Decision Tree
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression
- Random Forest
- XGBoost
- K-Nearest Neighbors (KNN)

The deployed application uses a **Random Forest classifier** for crop prediction.

### 🍃 Plant Disease Identification

The plant disease module uses a **Convolutional Neural Network (CNN)** to classify plant leaf images.

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

Users can upload a plant leaf image and receive a predicted disease class through the Streamlit application.

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────────┐
                         │        AgriNext         │
                         │     Web Interface       │
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
          Soil & Environmental                  Plant Leaf Image
              Parameters                              │
                     │                                  │
                     ▼                                  ▼
          ┌────────────────────┐             ┌──────────────────────┐
          │ Random Forest      │             │ CNN Deep Learning    │
          │ Classifier         │             │ Model                │
          └──────────┬─────────┘             └──────────┬───────────┘
                     │                                  │
                     ▼                                  ▼
              Recommended Crop                  Disease Prediction