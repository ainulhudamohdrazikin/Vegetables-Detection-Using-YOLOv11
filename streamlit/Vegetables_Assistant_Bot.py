
#%%
import streamlit as st
import requests
from PIL import Image
import os
import numpy as np

BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "35e2fffd-90a1-4ac3-acbd-4750ac8eca9e"
ENDPOINT = "vegetables" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    """
    Run a flow with a given message.

    :param message: The message to send to the flow
    :return: The JSON respons from the flow
    """

    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT or FLOW_ID}"

    payload = {
        "input_value": message,
        'output_type': 'chat',
        'input_type': 'chat',
    }

    response = requests.post(api_url, json=payload)
    return response.json()

#Function to extract the desired message
def extract_message(response: dict)-> str:
    try:
        #NAvigate to the message inside the response structure
        return response ['outputs'][0]['outputs'][0]['results']['message']['text']
    except (KeyError, IndexError):
        return 'No valid message found in response.'
    
#streamlit app
def main():
    st.title('🌿🥕 Welcome to the Smart Vegetable Detection System App! 🥦🍅')
    # st.logo('huda_pro2.jpg', size="large", link=None, icon_image=None)
    st.logo(r"C:\Users\User\Desktop\LangFlow\chroma db\ResumeHuda\linkedin_qrcode.jpg", size="large", link='https://www.linkedin.com/in/huda-razikin/', icon_image=None)
    st.sidebar.markdown("You may visit my LinkedIn by clicking the logo!")

    st.sidebar.write("🌿 VeggieVision: Smart Vegetable Detector 🍅") 
    st.sidebar.image(r"C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\Chroma_DB\veggie2.jpg", width=290,) 
    st.sidebar.write("Hello, veggie enthusiast! 🥳 You've entered a world where technology meets the garden! Our clever AI system can help you identify five popular vegetables with precision and ease. Just upload an image, and let our bot work its magic – it’s as easy as pie (or should we say, as easy as salad 😉)")
    st.sidebar.write("Whether you're a farmer, a chef, a curious gardener, or a health-conscious eater, our Smart Vegetable Detection System has you covered. Let’s dig in and uncover the wonders of the veggie world together! 🌱")
  
    #initialize session state for chat history
    if 'messages' not in st.session_state:
        st.session_state.messages =[]

    #Display previous messages into avatars
    for message in st.session_state.messages:
        with st.chat_message(message['role'], avatar=message['avatar']):
            st.write(message['content'])

    #input box for user message
    if query := st.chat_input("Ask me anything..."):
        #Add user message to session state
        st.session_state.messages.append(
            {
                'role':'user',
                'content': query,
                'avatar': '🥬', #emoji for user
            }
        )
        with st.chat_message('user', avatar='🥔'): #Display user message
            st.write(query)

        #Call the langflow API and get thhe assistant's response
        with st.chat_message('assistant', avatar=r"C:\Users\User\Desktop\AI_ML_TRAINING\YPAI09\Capstone\Capstone5(Final)\Chroma_DB\Veggie_Avatar.jpg"): #Emoji for assistant
            message_placeholder = st.empty() #placeholder for assistant response
            with st.spinner("Thinking..."):
                #Fetch response from Langflow
                assistant_response = extract_message(run_flow(query))
                message_placeholder.write(assistant_response)

        #Add assistant response to session state
        st.session_state.messages.append(
            {
                'role':'assistant',
                'content': assistant_response,
                'avatar': "🤖" 
                , #emoji for assistant
            }
        )

    st.write("Please rate this chatbot's performance.🥰") 
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
        st.markdown(f"Thank you for your feedback.🤩")
        st.snow()
    

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
