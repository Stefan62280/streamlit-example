import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Chatbot basique (POC MEL)')

openai_api_key = st.sidebar.text_input('OpenAI API Key')
System_prompt = st.sidebar.text_imput('test')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Posez une question ici')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Renseignez la clé API OpenAI!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
