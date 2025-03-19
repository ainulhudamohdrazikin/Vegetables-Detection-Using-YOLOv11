# Vegetables-Detection-Using-YOLOv11-VEGGIEVISION-

## **Description:**
VeggieVision is an AI-powered vegetable detection system designed to identify and classify vegetables in real-time. Built using YOLOv11, this project aims to achieve high accuracy (>0.80 mAP) while maintaining an inference time of <100ms per image on CPU.

📊 Dataset & Training Details
Dataset Size: 641 images (70% Train, 15% Validation, 15% Test)
Preprocessing: Images resized to 640x640 pixels, augmented with flips, rotations, and brightness adjustments.
Training Config: 30 epochs, input image size 240x240 pixels, horizontal flips, and shear augmentation.

## **Model Architecture:**
![model_architecture](https://github.com/user-attachments/assets/95315836-2415-4843-af30-ba633ff3d9fd)

## **Results:**
![result_30epoch_final](https://github.com/user-attachments/assets/3f0aaac0-9372-43af-857f-0833c21f1f93)
![tensorboard_box_loss](https://github.com/user-attachments/assets/e6c9b61c-a65b-46b0-aec5-92c6f95aff93)
![tensorboard_mAP](https://github.com/user-attachments/assets/73204b71-5489-4f4f-8959-12ae36693d1e)
![result_img](https://github.com/user-attachments/assets/13979ab3-03ac-4a9f-8b38-1d3b245bb1d4)

Before Model Training
![BEFORE](https://github.com/user-attachments/assets/3eb78e47-88ea-4a68-92c9-13bb8127cb35)

After Model Training
![result_latest](https://github.com/user-attachments/assets/5da008ba-d515-4064-893b-58e35fbf6a0d)

Webcam
![result_webcam](https://github.com/user-attachments/assets/25a69191-ddb1-40fc-92e1-1e26d3513522)


## **Discussion:**
As from the result can be conclude:-
✅ Real-Time Detection – Accurately classifies tomatoes, potatoes, cucumbers, cabbages, and cauliflowers.
✅ Optimized YOLOv11 Model – Trained with 641 annotated images, leveraging data augmentation techniques for robustness.
✅ High Accuracy – Achieves reliable detection with 30 training epochs and strategic augmentation methods.
✅ Streamlit App Deployment – User-friendly interface for real-time vegetable identification.

🚀 Future Enhancements
🔹 Expand detection to include more vegetable types.
🔹 Optimize model for mobile deployment.
🔹 Improve detection under varying lighting conditions.

## **Credit:**
The source of the datasets are from Kaggle and Google Images.
Check out the dataset by just one click away 😇 :   [Datasets](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)
