import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Title of the application
st.title("Image Text Extraction with EasyOCR")

# Upload image through Streamlit
uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

# Specify the path where you have downloaded the models
model_path = 'english.pth'

# Instantiate the EasyOCR Reader with the model path
reader = easyocr.Reader(['en'], model_storage_directory=model_path)  # Replace with the actual language codes

if uploaded_image is not None:
    # Load the image
    image = Image.open(uploaded_image)
    img_array = np.array(image)

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR using EasyOCR
    st.write("Extracting text from image...")
    result = reader.readtext(img_array)

    # Display OCR results as plain text
    st.subheader("Extracted Text:")
    
    # Collect all detected text in one output string
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + "\n"
    
    # Display the extracted text
    st.text(extracted_text)
