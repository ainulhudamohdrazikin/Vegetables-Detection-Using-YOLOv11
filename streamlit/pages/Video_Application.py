#%%
import streamlit as st
import requests
from PIL import Image
import os
import numpy as np
from ultralytics import YOLO
import yolo_model 
from ultralytics import solutions
import cv2
import yolo_model


# Image upload component
solutions.inference(model=r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt')

# Footer
st.markdown("---")
st.markdown("**Vegetable Detection System** | Developed with YOLOv11 and Streamlit")
st.write("🔍 **Confidence Threshold** helps control detection accuracy.")
st.write("© 2024 Vegetable AI Solutions by Ainul Huda Mohd Razikin")

# Decorative emojis and closing message
st.markdown("🥕🍅🍆🥒 Thank you for using the Vegetable Detection System! 🍅🥕🍆🥒")
# uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"],accept_multiple_files=True)
# if uploaded_file:
#         # Load the image
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", channels="BGR", use_column_width=True)
#         st.write("Detecting...")

#             # Convert PIL image to a format YOLO can process (e.g., numpy array)
#         image_np = np.array(image)

#             # Call the YOLO detection function
            
#         detected_image, detection_results = yolo_model.detect_objects(image_np)

#             # Display the output
#         st.image(detected_image, caption="Detection Results", channels="BGR", use_column_width=True)
#         st.write("Detection Details:")
#         st.write(detection_results)

# def detect_objects(yolo_model, image):
#         image_np = np.array(image)  # Convert PIL image to NumPy
#         results = yolo_model.predict(image_np)  # Replace with YOLOv11 detection method
#         detected_image = results.render()[0]  # Replace as needed for your YOLOv11
#         return detected_image, results

# if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", channels="BGR", use_column_width=True)
#             # Perform object detection
#         detected_image, detection_results = detect_objects(yolo_model, image)
#              # Display detected image
#         st.image(detected_image, caption="Detected Image", channels="BGR", use_column_width=True)

# img_files = st.file_uploader(label="Choose an image files",
#                  type=['png', 'jpg', 'jpeg'],
#                  accept_multiple_files=True)


# # function to convert file buffer to cv2 image
# def create_opencv_image_from_stringio(img_stream, cv2_img_flag=1):
#     img_stream.seek(0)
#     img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
#     return cv2.imdecode(img_array, cv2_img_flag)

# for n, img_file_buffer in enumerate(img_files):
#   if img_file_buffer is not None:

#     # 1) image file buffer will converted to cv2 image
#     open_cv_image = create_opencv_image_from_stringio(img_file_buffer)
#     # 2) pass image to the model to get the detection result
    
#     im0 = yolo_model(source=open_cv_image,
#               weights=r"C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt")

#     # 3) show result image using st.image()
#     if im0 is not None:
#         st.image(im0, 
#                 channels="BGR", \
#                 caption=f'Detection Results ({n+1}/{len(img_files)})'
#                 )
#     pass


# # %%
