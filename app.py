from tensorflow.keras.models import load_model
import gradio as gr
import numpy as np
from PIL import Image

# Load categories (manually define them or load from file)
categories = ['Pepper__bell___Bacterial_spot', 'Potato___healthy', 'Tomato_Leaf_Mold', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato_Bacterial_spot', 'Tomato_Septoria_leaf_spot', 'Tomato_healthy', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Early_blight', 'Tomato__Target_Spot', 'Pepper__bell___healthy', 'Potato___Late_blight', 'Tomato_Late_blight', 'Potato___Early_blight', 'Tomato__Tomato_mosaic_virus']

# Load model
model = load_model("model.h5")

# Prediction function
def predict_image(img):
    try:
        img = img.convert('RGB').resize((128, 128), Image.LANCZOS)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        top_indices = np.argsort(pred[0])[::-1][:3]
        return {categories[i]: float(pred[0][i]) for i in top_indices}
    except Exception as e:
        return {"Error": 1.0}

# Interface
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="🌿 Smart Crop Disease Detector",
    description="Upload a clear image of a plant leaf."
)

interface.launch()
