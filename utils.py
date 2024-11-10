from dotenv import load_dotenv
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import base64
from pathlib import Path

import os

load_dotenv()

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def cs_sidebar():
    # st.sidebar.header("Acesse as obras aqui:")
    pass
    # st.sidebar.markdown('https://www.insper.edu.br/')
