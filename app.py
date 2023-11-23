import string
import random
import streamlit as st
from hashlib import pbkdf2_hmac
from base64 import b64encode

def hash_password(password: str, target: str, salt: str, upper_limit: int=44) -> str:
    iter = 500_000
    original_key = b64encode(bytes(f'{target+password+salt}', 'utf-8'))
    enc_key = pbkdf2_hmac('sha256', original_key, bytes(f'{salt}', 'utf-8') * 2, iter)
    return b64encode(enc_key).decode("utf-8")[:upper_limit]

def lower_case():
    return list(string.ascii_lowercase)

def upper_case():
    return list(string.ascii_uppercase)

def symbols():
    return list(string.punctuation)

def numbers():
    return list(string.digits)

def make_list_modifiers(options: dict=None) -> list:
  if not options:
    options = {
        lower_case: True,
        upper_case: True,
        symbols: True,
        numbers: True
    }

  list_modifiers = []
  for key, value in options.items():
    if value:
      list_modifiers.append(key())

  flattened = [val for sublist in list_modifiers for val in sublist]
  random.Random(42).shuffle(flattened)
  return flattened, len(flattened)

def vigenere(password: str, key: str, options: dict) -> str:
  if len(key) < len(password):
    key += key
  key = key[:len(password)]
  
  list_modifier, len_modifier = make_list_modifiers(options)
  complete_modifiers, len_complete_modifiers = make_list_modifiers()
  cipher = ""
  for password_char, key_char in zip(password, key):
    index_password = complete_modifiers.index(password_char)
    index_key = complete_modifiers.index(key_char)
    offset = (index_password + index_key) % len_modifier
    cipher += list_modifier[offset]
  return cipher

st.write('Purple Chocolate - Gerador de senhas')
st.sidebar.slider('Tamanho da senha',0,44,44, key="upper_limit")
st.sidebar.checkbox('Letras minusculas', value=True, key='lower_case')
st.sidebar.checkbox('Letras maisuculas', value=True, key='upper_case')
st.sidebar.checkbox('Símbolos', value=True, key='symbols')
st.sidebar.checkbox('Números', value=True, key='numbers')

options = {
   lower_case: st.session_state.lower_case,
   upper_case: st.session_state.upper_case,
   symbols: st.session_state.symbols,
   numbers: st.session_state.numbers
}

st.text_input('Site da senha', key="target")
st.text_input('Digite uma senha fácil de lembrar', key="password")
st.text_input('Digite uma informação extra que deseja colocar na senha. Pode deixar em branco', key="salt")

password = st.session_state.password
target = st.session_state.target
salt = st.session_state.salt
upper_limit = st.session_state.upper_limit
password = hash_password(password, target, salt, upper_limit)
password = vigenere(password, salt, options)

st.write("Sua senha forte é")
st.write(f'{password}')