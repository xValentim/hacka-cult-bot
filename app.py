import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons

# if 'authentication_status' not in ss:
#     st.switch_page('./pages/account.py')

MenuButtons()
st.header('Home page')

# Protege o conteudo da pagina.
# if ss.authentication_status:
#     st.write('Esse conteúdo só é acessível para usuários logados.')
# else:
#     st.write('Por favor efetue o login.')