# 🌿 Smart Plant Disease Detector

<p align="center">
  <strong>An AI-powered web application that detects plant leaf diseases using Deep Learning.</strong>
</p>

<p align="center">
  Upload a leaf image and receive the predicted disease along with the model's confidence scores.
</p>

---

## 📖 Overview

Smart Plant Disease Detector is a Deep Learning application that helps identify common diseases affecting **Tomato**, **Potato**, and **Bell Pepper** plants.

The system uses a trained TensorFlow/Keras model and provides predictions through an interactive Gradio interface.

---

## ✨ Features

- 🌱 Detects multiple plant diseases
- 📸 Upload leaf images directly
- 🤖 Deep Learning based classification
- 📊 Displays Top-3 predictions with confidence scores
- ⚡ Simple and intuitive Gradio interface

---

## 🛠 Tech Stack

### Programming Language

- Python

### AI & Machine Learning

- TensorFlow
- Keras
- NumPy

### Interface

- Gradio

### Image Processing

- Pillow (PIL)

---

## 🌾 Supported Classes

- Pepper Bell Healthy
- Pepper Bell Bacterial Spot
- Potato Healthy
- Potato Early Blight
- Potato Late Blight
- Tomato Healthy
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Septoria Leaf Spot
- Tomato Target Spot
- Tomato Bacterial Spot
- Tomato Yellow Leaf Curl Virus
- Tomato Mosaic Virus
- Tomato Spider Mites

---

## 📂 Project Structure

```text
Smart_Plant_disease_detector/
│
├── app.py
├── model.h5
├── requirements.txt
├── README.md
└── Plant_disease_detector.h5
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Smart_Plant_disease_detector.git
```

Move into the project directory

```bash
cd Smart_Plant_disease_detector
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

## 📊 Dataset

The model was trained using the **Plant Disease Dataset** from Kaggle, containing labeled images of healthy and diseased plant leaves across multiple crop species.

**Dataset Source:**
https://www.kaggle.com/datasets/emmarex/plantdisease

The dataset includes diseases affecting crops such as:

* 🍅 Tomato
* 🥔 Potato
* 🫑 Bell Pepper

It covers multiple disease categories, including healthy leaves, enabling the model to learn robust image classification patterns.

---

## 🚀 Live Demo

Experience the application directly through Hugging Face Spaces:

👉 https://huggingface.co/spaces/Nxsib/plant-disease-detector

Simply upload a leaf image and the model will predict the most likely disease along with confidence scores.

---

## 📓 Model Development

The complete training workflow—including data preprocessing, model training, evaluation, and experimentation—is available on Kaggle:

👉 https://www.kaggle.com/code/nasibyun/smart-plant-disease-detector



## 🚀 Usage

1. Launch the application.
2. Upload a clear image of a plant leaf.
3. The model analyzes the image.
4. View the top predicted diseases with confidence scores.

---

## 📦 Requirements

- Python 3.9+
- TensorFlow
- Gradio
- NumPy
- Pillow

---

## 🔮 Future Improvements

- Disease treatment recommendations
- Mobile-friendly interface
- Support for additional crops
- Real-time camera detection
- Model performance dashboard

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is intended for educational and research purposes.
