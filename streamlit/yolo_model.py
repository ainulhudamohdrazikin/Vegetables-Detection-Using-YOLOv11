#%%
#1. Import packages

import ultralytics
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt
import cv2

#%%
#2. Load the pretrained model
model = YOLO('yolo11x.pt')
#%%
# r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt'
model_custom = YOLO( r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt')#%%

def detect_objects(model_custom, image):
    image_np = np.array(image)  # Convert image to NumPy if needed
    results = model_custom.predict(image_np)  # Assuming `predict` is the correct method
    detected_image = [results.render()[0] for res in results]  # Modify if needed
    return detected_image, results

# def detect_objects(model_custom, image):
#     # Perform detection
#     # model_custom = ov_model( r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt')
#     results = model_custom(image_np)
#     # Parse the results for display
#     detected_image = [results.render()[0] for res in results]  # Get annotated image
#     return detected_image, results.pandas().xyxy[0]  # Return image and details as DataFrame


# Export the model
model.export(format="onnx", dynamic=True)
# %%
