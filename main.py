import streamlit as st
import easyocr
import cv2
from PIL import Image
import numpy as np

# Title of the application
st.title("Image Text Extraction with EasyOCR")

# Upload image through Streamlit
uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

# Instantiate the EasyOCR Reader
reader = easyocr.Reader(['en'])  # You can add more languages if needed

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

