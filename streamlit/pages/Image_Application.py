#%%
import streamlit as st
import torch
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

def main():
    st.title('🌿🥕 Let’s experience the Vegetable Detection System App! 🥦🍅')
    # st.logo('huda_pro2.jpg', size="large", link=None, icon_image=None)
    st.logo(r"C:\Users\User\Desktop\LangFlow\chroma db\ResumeHuda\linkedin_qrcode.jpg", size="large", link='https://www.linkedin.com/in/huda-razikin/', icon_image=None)
    st.sidebar.markdown("You may visit my LinkedIn by clicking the logo!")

    st.sidebar.write("🌿 VeggieVision: Smart Vegetable Detector 🍅") 
    st.sidebar.image(r"C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\Chroma_DB\veggie2.jpg", width=290,) 
    st.sidebar.write("Hello, veggie enthusiast! 🥳 You've entered a world where technology meets the garden! Our clever AI system can help you identify five popular vegetables with precision and ease. Just upload an image, and let our bot work its magic – it’s as easy as pie (or should we say, as easy as salad 😉)")
    st.sidebar.write("Whether you're a farmer, a chef, a curious gardener, or a health-conscious eater, our Smart Vegetable Detection System has you covered. Let’s dig in and uncover the wonders of the veggie world together! 🌱")
  
if __name__ =='__main__':
    main()

# Load the YOLO model (YOLOv5 or YOLOv7 can be loaded from TorchHub)
@st.cache_resource  # Cache the model to load it only once
def load_model():
    model = YOLO( r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt')
    return model

def detect_objects(image, model):
    # Convert the input image to RGB format if it isn't already
    img = np.array(image.convert("RGB"))
    
    # Run detection - YOLO may return a list, even if we're passing a single image
    results = model([img])  # Pass image as a list to ensure compatibility
    
    # Retrieve the first result from the list, then call plot()
    annotated_img = results[0].plot()  # Get the annotated image from the first result
    
    # Convert the annotated image (NumPy array) to a PIL image for Streamlit display
    return Image.fromarray(annotated_img)


# Streamlit App
st.write("Upload a picture of vegetables, and our AI model will detect each vegetable in the image.")

# Image uploader
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Load YOLO model
model = load_model()

if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Run detection
    st.write("Detecting objects...")
    result_image = detect_objects(image, model)
    
    # Display the result image with bounding boxes
    st.image(result_image, caption="Detected Objects", use_column_width=True)
else:
    st.write("Please upload an image to start object detection.")

# Footer
st.markdown("---")
st.markdown("**Vegetable Detection System** | Developed with YOLOv11 and Streamlit")
st.write("🔍 **Confidence Threshold** helps control detection accuracy.")
st.write("© 2024 Vegetable AI Solutions by Ainul Huda Mohd Razikin")

# Decorative emojis and closing message
st.markdown("🥕🍅🍆🥒 Thank you for using the Vegetable Detection System! 🍅🥕🍆🥒")


# %%
