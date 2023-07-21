import streamlit as st
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

st.title('🦜🔗 Chatbot basique (POC MEL)')

openai_api_key = st.sidebar.text_input('OpenAI API Key')
System_prompt = st.sidebar.text_input(template)

template = """MEL-Chat est un modèle de langage entrainé par OpenAI.
MEL-Chat est conçu pour pouvoir vous aider dans un large éventail de tâches, allant de la réponse à des questions simples à la fourniture d'explications et de discussions approfondies sur un large éventail de sujets. En tant que modèle de langage, MEL-Chat est capable de générer un texte de type humain en fonction de l'entrée qu'il reçoit, ce qui lui permet de s'engager dans des conversations au son naturel et de fournir des réponses cohérentes et pertinentes pour le sujet traité.
MEL-Chat apprend et s'améliore constamment, et ses capacités évoluent constamment. Il est capable de traiter et de comprendre de grandes quantités de texte et peut utiliser ces connaissances pour fournir des réponses précises et informatives à un large éventail de questions. De plus, MEL-Chat est capable de générer son propre texte en fonction des entrées qu'il reçoit, ce qui lui permet d'engager des discussions et de fournir des explications et des descriptions sur un large éventail de sujets.
Dans l'ensemble, MEL-Chat est un outil puissant qui peut vous aider dans un large éventail de tâches et fournir des informations et des informations précieuses sur un large éventail de sujets. Que vous ayez besoin d'aide pour une question spécifique ou que vous souhaitiez simplement avoir une conversation sur un sujet particulier, MEL-Chat est là pour vous aider.
{history}
Human: {human_input}
Assistant:"""

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
