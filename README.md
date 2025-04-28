# Fake Currency Detection Using Deep Learning

## Project Description
This project uses a deep learning model (ResNet50-based) to classify Indian currency notes as **Real** or **Fake**.  
It leverages data augmentation techniques and transfer learning to achieve good accuracy.

---

## Technologies Used
- Python
- TensorFlow / Keras
- ResNet50 (pretrained on ImageNet)
- Flask (for web deployment)
- HTML/CSS (frontend)

---

## Dataset
- Images of real and fake currency notes (Rs. 2000 and Rs. 500 denominations).
- The dataset is divided into:
  - **Training set** (with augmentation)
  - **Validation set**

---

## Model Details
- **Base Model**: ResNet50 without top layers (`include_top=False`).
- **Custom Top Layers**: 
  - Flatten
  - Dense Layers (1024, 1024 units)
  - Dropout (0.5)
  - Output Layer (Softmax Activation)

- **Input Shape**: (300, 300, 3)

- **Batch Size**: 8

- **Loss Function**: Categorical Cross-Entropy
- **Optimizer**: Adam Optimizer

---

## Augmentation Techniques
- Rotation (up to 90 degrees)
- Horizontal flip
- Vertical flip
- Preprocessing according to ResNet50 standards

---

## How to Run
1. Install requirements
2. Train the model or load a pretrained one.
3. Run the Flask app.
4. Upload a currency note image to predict if it is Real or Fake.

---

## Future Improvements
- Add more note denominations (e.g., Rs. 100, Rs. 50).
- Detect color-printed fake notes.
- Improve UI/UX for better user interaction.

---

## Author
Created with ❤️ for learning purposes.
