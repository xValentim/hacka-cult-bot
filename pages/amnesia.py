from dotenv import load_dotenv
import streamlit as st
import os
import streamlit.components.v1 as components

# Langchain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import time

from utils import *
from src.chains_amnesia import *
from streamlit import session_state as ss
from modules.nav import MenuButtons

load_dotenv()

# if 'authentication_status' not in ss:
#     st.switch_page('./pages/account.py')

MenuButtons()

# app config
st.title("Chatbot - Amnésia")
# st.subheader("Olá, sou uma IA do Masp. Gostaria de saber mais sobre a obra Amnésia de Flávio Cerqueira?")
cs_sidebar()



# components.iframe(f"https://splat-vis-production.up.railway.app/index.html{st.session_state.url_splat}", height=640)
components.iframe("https://lumalabs.ai/embed/e6648ddb-3bc2-4f8e-84bb-12d42b4731bc?mode=sparkles&background=%23ffffff&color=%23000000&showTitle=true&loadBg=true&logoPosition=bottom-left&infoPosition=bottom-right&cinematicVideo=undefined&showMenu=false", height=720)

# session state
if "chat_history_amnesia" not in st.session_state:
    st.session_state.chat_history_amnesia = [
        AIMessage(content="Olá, sou uma IA. Gostaria de saber mais sobre a obra Amnésia de Flávio Cerqueira?"),
    ]

# conversation
for message in st.session_state.chat_history_amnesia:
    if isinstance(message, AIMessage):
        with st.chat_message("AI", avatar="🤖"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human", avatar="👤"):
            st.write(message.content)
            
# user input

user_query = st.chat_input("Digite algo...")

if user_query is not None and user_query != "":
    
    st.session_state.chat_history_amnesia.append(HumanMessage(content=user_query))

    with st.chat_message("Human", avatar="👤"):
        st.markdown(user_query)

    with st.chat_message("AI", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = st.write_stream(chain.stream({"input": user_query}))
        
    st.session_state.chat_history_amnesia.append(AIMessage(content=str(response)))
