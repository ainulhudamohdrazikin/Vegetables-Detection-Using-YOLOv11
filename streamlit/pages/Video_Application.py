#%%
import streamlit as st
from PIL import Image
import os
from ultralytics import solutions


# Image upload component
solutions.inference(model=r'C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\runs\detect\train27\weights\best.pt')
def main():
    st.logo(r"C:\Users\User\Desktop\LangFlow\chroma db\ResumeHuda\linkedin_qrcode.jpg", size="large", link='https://www.linkedin.com/in/huda-razikin/', icon_image=None)
if __name__ =='__main__':
    main()
    
# Footer
st.markdown("---")
st.markdown("**Vegetable Detection System** | Developed with YOLOv11 and Streamlit")
st.write("🔍 **Confidence Threshold** helps control detection accuracy.")
st.write("© 2024 Vegetable AI Solutions by Ainul Huda Mohd Razikin")

# Decorative emojis and closing message
st.markdown("🥕🍅🍆🥒 Thank you for using the Vegetable Detection System! 🍅🥕🍆🥒")


# %%
