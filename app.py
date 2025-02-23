import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load Model
MODEL_PATH = "model/potatoes.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Constants
IMAGE_SIZE = (256, 256)
LABELS = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

# Function to Process Image
def process_image(img):
    img = img.resize(IMAGE_SIZE, Image.LANCZOS)  # Better resizing
    img = np.array(img) / 255.0  # Normalize
    return img

# Function to Predict
def predict(model, img):
    img_array = tf.convert_to_tensor(img, dtype=tf.float32)
    img_array = tf.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    pred_class = LABELS[np.argmax(pred[0])]
    confidence = round(100 * np.max(pred[0]), 2)
    return pred_class, confidence

# Streamlit App Title
st.title("🍂 Potato Disease Classifier")
st.write("Upload an image of a potato leaf, and the model will classify it!")

# Sidebar for Instructions
st.sidebar.header("📌 How to Use")
st.sidebar.info("1️⃣ Upload an image of a potato leaf 📷\n"
                "2️⃣ Model will analyze it 🔬\n"
                "3️⃣ Get the disease prediction 🚀")

# File Upload Section
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display Uploaded Image
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_container_width=True)

    # Preprocess & Predict
    processed_image = process_image(image)
    predicted_label, confidence = predict(model, processed_image)

    # Display Prediction
    st.subheader("🎯 Prediction Result")
    
    st.success(f"**{predicted_label}** (Confidence: {confidence:.2f}%)")
