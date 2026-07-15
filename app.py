from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model = load_model("models/handwritten_digit_model.keras")

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Preprocess image
    img = Image.open(filepath).convert("L")
    img = img.resize((28, 28))

    img = np.array(img)

    # Invert image (black background, white digit)
    img = 255 - img

    img = img / 255.0

    img = img.reshape(1, 28, 28)

    prediction = model.predict(img)

    digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    return render_template(
        "result.html",
        digit=digit,
        confidence=round(confidence, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)