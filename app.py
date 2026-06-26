from tensorflow.keras.models import load_model
import gradio as gr
import numpy as np
from PIL import Image

model = load_model("model.h5")

categories = [
    "Pepper__bell___Bacterial_spot",
    "Potato___healthy",
    "Tomato_Leaf_Mold",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato_Bacterial_spot",
    "Tomato_Septoria_leaf_spot",
    "Tomato_healthy",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato_Early_blight",
    "Tomato__Target_Spot",
    "Pepper__bell___healthy",
    "Potato___Late_blight",
    "Tomato_Late_blight",
    "Potato___Early_blight",
    "Tomato__Tomato_mosaic_virus"
]

# -----------------------------
# Format Class Names
# -----------------------------
def pretty_name(name):
    name = name.replace("___", " - ")
    name = name.replace("__", " ")
    name = name.replace("_", " ")
    return name.title()

# -----------------------------
# Prediction Function
# -----------------------------
def predict(image):
    if image is None:
        return {"Please upload an image": 1.0}

    image = image.convert("RGB")
    image = image.resize((128, 128), Image.LANCZOS)

    img = np.array(image, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)[0]

    top = np.argsort(prediction)[::-1][:3]

    return {
        pretty_name(categories[i]): float(prediction[i])
        for i in top
    }

# -----------------------------
# Theme
# -----------------------------
theme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="emerald"
)

css = """
.gradio-container{
    max-width:1100px !important;
    margin:auto;
}

footer{
    display:none;
}

h1{
    text-align:center;
}

.gr-button-primary{
    font-size:18px;
}
"""

# -----------------------------
# Interface
# -----------------------------
with gr.Blocks(theme=theme, css=css) as demo:

    gr.Markdown(
        """
# 🌿 Smart Plant Disease Detector

### AI-powered CNN model trained on the PlantVillage Dataset

Upload a clear image of a **Tomato**, **Potato**, or **Bell Pepper** leaf and receive the **Top-3 predictions** with confidence scores.
"""
    )

    with gr.Row():

        with gr.Column(scale=1):
            image = gr.Image(
                type="pil",
                label="📷 Upload Plant Leaf"
            )

            predict_btn = gr.Button(
                "🔍 Analyze Leaf",
                variant="primary"
            )

        with gr.Column(scale=1):
            output = gr.Label(
                num_top_classes=3,
                label="🩺 Prediction"
            )

    predict_btn.click(
        fn=predict,
        inputs=image,
        outputs=output
    )

demo.launch()
