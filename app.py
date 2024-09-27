import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE-API-KEY')
genai.configure(api_key = GOOGLE_API_KEY)
st.title("IMAGE TO TEXT APPLICATION")
user_text = st.text_input('input Prompt :')

uploaded_file = st.file_uploader("Upload file :", type = ["jpg","jpeg","png"])

#display image
from PIL import Image
img = ""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="uploaded img")

#img evalution

def gemini_response(img, user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if user_input!="":
        response = model.generate_content([user_input, img])
    else:
        response = model.generate_content(img)
    return response.text

submit = st.button("button")

if submit:
    response = gemini_response(user_input=user_text, img=img)
    st.subheader("Respones is")
    st.write(response)

