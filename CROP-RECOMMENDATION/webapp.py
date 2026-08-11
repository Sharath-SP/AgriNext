import streamlit as st
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
from PIL import Image


# --------------------------------------------------
# Base directory
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent


# --------------------------------------------------
# Load trained Random Forest model
# --------------------------------------------------
MODEL_PATH = BASE_DIR / "RF.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Unable to load crop recommendation model: {e}")
    st.stop()


# --------------------------------------------------
# Optional crop image
# --------------------------------------------------
def show_crop_image(crop_name: str) -> None:
    """
    Display crop image if available.
    Expected location:
    CROP-RECOMMENDATION/crop_images/<crop_name>.jpg
    """

    image_path = BASE_DIR / "crop_images" / f"{crop_name.lower()}.jpg"

    if image_path.exists():
        try:
            img = Image.open(image_path)
            st.image(
                img,
                caption=f"Recommended crop: {crop_name}",
                width="stretch"
            )
        except Exception:
            st.warning("Crop image exists but could not be opened.")
    else:
        st.info("No image available for this crop (optional).")


# --------------------------------------------------
# Crop prediction
# --------------------------------------------------
def predict_crop(
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall
):
    inputs = np.array([
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]).reshape(1, -1)

    prediction = model.predict(inputs)

    return prediction[0]


# --------------------------------------------------
# Main application
# --------------------------------------------------
def main():

    st.markdown(
        "<h1 style='text-align: center;'>SMART CROP RECOMMENDATIONS</h1>",
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # Header image
    # --------------------------------------------------
    crop_image_path = BASE_DIR / "crop.png"

    if crop_image_path.exists():
        try:
            header_img = Image.open(crop_image_path)
            st.image(header_img)
        except Exception as e:
            st.warning(f"Header image could not be displayed: {e}")


    # --------------------------------------------------
    # Sidebar
    # --------------------------------------------------
    st.sidebar.title("AgriNext")
    st.sidebar.header("Enter Crop Details")

    nitrogen = st.sidebar.number_input(
        "Nitrogen",
        min_value=0.0,
        max_value=140.0,
        value=20.0,
        step=0.1
    )

    phosphorus = st.sidebar.number_input(
        "Phosphorus",
        min_value=0.0,
        max_value=145.0,
        value=20.0,
        step=0.1
    )

    potassium = st.sidebar.number_input(
        "Potassium",
        min_value=0.0,
        max_value=205.0,
        value=20.0,
        step=0.1
    )

    temperature = st.sidebar.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=51.0,
        value=25.0,
        step=0.1
    )

    humidity = st.sidebar.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.1
    )

    ph = st.sidebar.number_input(
        "pH Level",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1
    )

    rainfall = st.sidebar.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=0.1
    )


    # --------------------------------------------------
    # Prediction button
    # --------------------------------------------------
    if st.sidebar.button("Predict"):

        inputs = np.array([
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ])

        if np.isnan(inputs).any():
            st.error("Please enter valid values for all fields.")

        else:

            prediction = predict_crop(
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            )

            st.success(
                f"The recommended crop is: {prediction}"
            )

            show_crop_image(str(prediction))


    st.write(
        "Crop recommendation is generated using a trained "
        "Random Forest machine learning model."
    )


# --------------------------------------------------
# Run application
# --------------------------------------------------
if __name__ == "__main__":
    main()