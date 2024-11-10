import streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from modules.nav import MenuButtons


CONFIG_FILENAME = 'config.yaml'

with open(CONFIG_FILENAME) as file:
    config = yaml.load(file, Loader=SafeLoader)

st.header('Login')

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# login_tab, register_tab = st.tabs(['Login','Registrar'])

# with login_tab:
authenticator.login(location='main')

if ss["authentication_status"]:
    authenticator.logout(location='main')    
    st.write(f'Bem vindo *{ss["name"]}*')

elif ss["authentication_status"] is False:
    st.error('Username/senha está errado')
elif ss["authentication_status"] is None:
    st.warning('Por favor insira seu username e senha')

# with register_tab:
#     if not ss["authentication_status"]:
#         try:
#             email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()
#             if email_of_registered_user:
#                 st.success('Usuário registrado com sucesso')
#         except Exception as e:
#             st.error(e)

# We call below code in case of registration, reset password, etc.
with open(CONFIG_FILENAME, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

# Call this late because we show the page navigator depending on who logged in.
MenuButtons()