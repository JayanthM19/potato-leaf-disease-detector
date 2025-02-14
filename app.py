import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


MODEL_PATH = "model.h5"  
model = tf.keras.models.load_model(MODEL_PATH)


CLASS_NAMES = ["Early Blight", "Healthy", "Late Blight"]


st.title("🥔 Potato Leaf Disease Detection")
st.write("Upload a potato leaf image to predict its health status.")


uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
   
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    
    img = image.resize((224, 224)) 
    img_array = np.array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0) 

   
    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]

  
    st.success(f"Prediction: **{predicted_class}**")
