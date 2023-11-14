import streamlit as st
from hashlib import pbkdf2_hmac
from base64 import b64encode

def hash_password(password: str, target: str, salt: str, upper_limit: int=44) -> str:
    iter = 500_000
    original_key = b64encode(bytes(f'{target+password+salt}', 'utf-8'))
    enc_key = pbkdf2_hmac('sha256', original_key, bytes(f'{salt}', 'utf-8') * 2, iter)
    return b64encode(enc_key).decode("utf-8")[:upper_limit]

st.write('Purple Chocolate - Gerador de senhas')
st.sidebar.slider('Tamanho da senha',0,44,44, key="upper_limit")

st.text_input('Site da senha', key="target")
st.text_input('Digite uma senha fácil de lembrar', key="password")
st.text_input('Digite uma informação extra que deseja colocar na senha. Pode deixar em branco', key="salt")

password = st.session_state.password
target = st.session_state.target
salt = st.session_state.salt
upper_limit = st.session_state.upper_limit

st.write("Sua senha forte é")
st.write(f'{hash_password(password, target, salt, upper_limit)}')