from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("Final_model.h5")  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html')  # Main upload page

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        img_path = os.path.join("static", file.filename)
        file.save(img_path)

        img = image.load_img(img_path, target_size=(300, 300))
        img_array = np.asarray(img)
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        label = "Fake" if prediction[0][0] > prediction[0][1] else "Real"

        return render_template('result.html', prediction=label, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
