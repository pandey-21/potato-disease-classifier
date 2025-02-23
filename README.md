# 🍠 Potato Disease Classification

## 📌 Overview
This project classifies potato leaf diseases using a Convolutional Neural Network (CNN). A web interface built with **Streamlit** allows users to upload images and get disease predictions.

## 🚀 Live Demo
🔗 https://potato-disease-classifier-7mtvaykmr4cipsymbwbqnr.streamlit.app/

## 📂 Project Structure
```
├── dataset/                # Dataset (or link below)
├── notebooks/              # Jupyter notebooks
├── app/                    # Streamlit app code
├── models/                 # Trained models
├── README.md               # Documentation
├── requirements.txt        # Dependencies
```

## 📊 Dataset
- **Classes:** Healthy, Early Blight, Late Blight

## 🏗️ Model
- **Base Model:** CNN 
- **Input Shape:** (256x256)
- **Optimizer:** Adam

## 💻 Installation
```bash
git clone https://github.com/pandey-21/potato-disease-classification.git
cd potato-disease-classification
pip install -r requirements.txt
streamlit run app/app.py
```

## 📦 Deployment
Deployed using **Streamlit Cloud
