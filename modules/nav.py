import streamlit as st
from streamlit import session_state as ss

def HomeNav():
    st.sidebar.page_link("app.py", label="Home", icon='🏠')

def LoginNav():
    st.sidebar.page_link("pages/account.py", label="Account", icon='🔐')

def VenusNav():
    st.sidebar.page_link("pages/venus.py", label="Venus - Chat", icon='🎭')

def AmnesiaNav():
    st.sidebar.page_link("pages/amnesia.py", label="Amnésia - Chat", icon='🖌️')
    
def GiNav():
    st.sidebar.page_link("pages/gi.py", label="GI - Chat", icon='🎨')

def JoaoNav():
    st.sidebar.page_link("pages/joao_moura.py", label="João Moura - Chat", icon='🤖')

def DomNav():
    st.sidebar.page_link("pages/dom_casmurro.py", label="Dom - Chat", icon='🎨')

def MenuButtons():
    # if 'authentication_status' not in ss:
    #     ss.authentication_status = False

    # Sempre mostra a HOME e LOGIN.
    # HomeNav()
    # LoginNav()

    # # Se o usuário logar, mostra as demais telas.
    # if ss["authentication_status"]:
    st.sidebar.header("Acesse as obras aqui:")
    DomNav()
    VenusNav()
    AmnesiaNav()
    GiNav()
    JoaoNav()
