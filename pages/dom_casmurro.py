from dotenv import load_dotenv
import streamlit as st
import os
import streamlit.components.v1 as components

# Langchain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import time

from utils import *
# from src.chains_joao import *
from streamlit import session_state as ss
from modules.nav import MenuButtons
from operator import itemgetter

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

MenuButtons()

st.title("Chatbot - Dom Casmurro")
cs_sidebar()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=1536
)

def format_docs(docs):
    return "\n\n".join([x.page_content for x in docs])

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)


system_prompt = """
Você é um assistente de IA que vai tirar dúvidas do usuário sobre o livro Dom Casmurro. Lembre-se de responder as dúvidas dele com base no livro Dom Casmurro de Machado de Assis e que ele precisa estudar literatura para além do vestibular. Faça isso ser divertido.

Aqui está um contexto do livro que pode ajudar na resposta ao usuário: {context}
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

if 'db' not in st.session_state:
    st.session_state.aux = False
    st.session_state.db = FAISS.load_local("./vectorstore/dom_casmurro", 
                                            embeddings, 
                                            allow_dangerous_deserialization=True)
    st.session_state.retriever = st.session_state.db.as_retriever(search_kwargs={"k": 5})

chain = (
    {
        "context": itemgetter("input") | st.session_state.retriever | RunnableLambda(format_docs),
        "input": itemgetter("input")
    }
    | prompt 
    | llm 
    | StrOutputParser()
)


# session state
if "chat_history_dom_casmurro" not in st.session_state:
    st.session_state.chat_history_dom_casmurro = [
        AIMessage(content="Olá, sou uma IA. Gostaria de saber mais sobre o livro Dom Casmurro?"),
    ]

# conversation
for message in st.session_state.chat_history_dom_casmurro:
    if isinstance(message, AIMessage):
        with st.chat_message("AI", avatar="🤖"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human", avatar="👤"):
            st.write(message.content)
            
# user input

user_query = st.chat_input("Digite algo...")

if user_query is not None and user_query != "":
    
    st.session_state.chat_history_dom_casmurro.append(HumanMessage(content=user_query))

    with st.chat_message("Human", avatar="👤"):
        st.markdown(user_query)

    with st.chat_message("AI", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = st.write_stream(chain.stream({"input": user_query}))
        
    st.session_state.chat_history_dom_casmurro.append(AIMessage(content=str(response)))
