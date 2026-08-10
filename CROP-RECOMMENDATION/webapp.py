## Importing necessary libraries for the web app
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Display Images
## Importing necessary libraries for the web app
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import warnings
from sklearn import metrics
from sklearn.model_selection import train_test_split
from PIL import Image


warnings.filterwarnings('ignore')


# --- Utility: load dataset -------------------------------------------------
DATA_CSV = 'Crop_recommendation.csv'
if not os.path.exists(DATA_CSV):
    st.error(f"Required data file '{DATA_CSV}' not found in the app folder.")
    st.stop()

df = pd.read_csv(DATA_CSV)

# Features and label
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# --- Train model -----------------------------------------------------------
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=42)
RF = RandomForestClassifier(n_estimators=20, random_state=5)
RF.fit(Xtrain, Ytrain)
predicted_values = RF.predict(Xtest)
accuracy = metrics.accuracy_score(Ytest, predicted_values)


# --- Helper: show crop image -----------------------------------------------
def show_crop_image(crop_name: str) -> None:
    """Display a crop image if present in ./crop_images/<name>.jpg"""
    image_path = os.path.join('crop_images', f"{crop_name.lower()}.jpg")
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            st.image(img, caption=f"Recommended crop: {crop_name}", use_column_width=True)
        except Exception:
            st.warning("Found image but couldn't open it.")
    else:
        st.info("No image available for this crop (optional).")


# --- Persist the trained model ---------------------------------------------
RF_PKL = 'RF.pkl'
try:
    with open(RF_PKL, 'wb') as f:
        pickle.dump(RF, f)
except Exception as e:
    st.warning(f"Couldn't save trained model to '{RF_PKL}': {e}")

# Load the model for prediction (use the in-memory RF if load fails)
try:
    with open(RF_PKL, 'rb') as f:
        model = pickle.load(f)
except Exception:
    model = RF


def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    arr = np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]).reshape(1, -1)
    return model.predict(arr)


def main():
    # Title
    st.markdown("<h1 style='text-align: center;'>SMART CROP RECOMMENDATIONS</h1>", unsafe_allow_html=True)

    # Optional header image
    crop_image_path = "crop.png"
    if os.path.exists(crop_image_path):
        try:
            header_img = Image.open(crop_image_path)
            st.image(header_img, use_column_width=True)
        except Exception:
            st.warning("Optional header image exists but couldn't be opened.")

    st.sidebar.title("AgriNext")
    st.sidebar.header("Enter Crop Details")

    nitrogen = st.sidebar.number_input("Nitrogen", min_value=0.0, max_value=140.0, value=0.0, step=0.1)
    phosphorus = st.sidebar.number_input("Phosphorus", min_value=0.0, max_value=145.0, value=0.0, step=0.1)
    potassium = st.sidebar.number_input("Potassium", min_value=0.0, max_value=205.0, value=0.0, step=0.1)
    temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=51.0, value=0.0, step=0.1)
    humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=0.0, step=0.1)
    rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)

    st.sidebar.markdown("---")
    if st.sidebar.button("Predict"):
        inputs = np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall])
        if np.isnan(inputs).any() or (inputs == 0).all():
            st.error("Please fill in all input fields with valid non-zero values before predicting.")
        else:
            prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            st.success(f"The recommended crop is: {prediction[0]}")
            show_crop_image(str(prediction[0]))

    # show model accuracy on the page for context
    st.write(f"Trained model accuracy on hold-out: {accuracy:.3f}")


if __name__ == '__main__':
    main()
##this one old