# STREAMLIT
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.grid import grid
from st_keyup import st_keyup
import secp256k1
from Crypto.Hash import keccak
import os
import hashlib
import random
import numpy as np

# --- PAGE CONFIG (BROWSER TAB) ---
st.set_page_config(page_title="Toolbox", page_icon=":toolbox:", layout="centered", initial_sidebar_state="expanded")
    
# --- MAIN PAGE ---

# PASSWORD GENERATOR
def password_generator(_password_length, _password_characters):
    digit = '1234567890'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '!@#$%^&*()_+-='
    all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
    input_characters = ""
    for option in _password_characters:
        if option == '0~9':
            input_characters += digit
        if option == 'lower-case':
            input_characters += lower
        if option == 'UPPER-CASE':
            input_characters += upper
        if option == '!@#$':
            input_characters += special
    if len(input_characters)==0:
        return "Characters can't be empty!"
    strong_password = ''
    for x in range(_password_length):
        strong_password += random.choice(input_characters)
    return strong_password
    
# USER INTERFACE
with st.form("Password"):
    st.header("Strong Password Generator")
    layout = grid([1,4], vertical_align="center")
    password_length = layout.number_input('Lenght (Max:64)', min_value=3, max_value=64, value=16, step=1)
    password_characters = layout.multiselect( 'Select character options',['0~9', 'lower-case', 'UPPER-CASE', '!@#$'], ['0~9', 'lower-case', 'UPPER-CASE', '!@#$'])
    if st.form_submit_button("Generate Strong Password", use_container_width=True):
        password = password_generator(password_length, password_characters)
        st.code(password, language="http")
        
st.divider()


# LEET GENERATOR
def leet_encoder(string):
    leet_dict = { "i":"1", "z":"2", "e":"3", "a":"4", "s":"5", "g":"6", "t":"7", "b":"8", "q":"9", "o":"0"}
    leet_string = ""
    for char in string:
        if char in leet_dict:
            leet_string += leet_dict[char]
        else:
            leet_string += char
    return leet_string
    
def leet_decoder(string):
    leet_dict = { "1":"i", "2":"z", "3":"e", "4":"a", "5":"s", "6":"g", "7":"t", "8":"b", "9":"q", "0":"o"}
    leet_string = ""
    for char in string:
        if char in leet_dict:
            leet_string += leet_dict[char]
        else:
            leet_string += char   
    return leet_string
    
# USER INTERFACE
with st.form("Leet"):
    st.header("Leet Language Translator")
    layout = grid([1,4], vertical_align="center")
    mode = layout.selectbox('Mode',('Encoder', 'Decoder'))
    input = layout.text_input("Input", value="")
    if st.form_submit_button("Submit", use_container_width=True):
        if mode=="Encoder":
            output = leet_encoder(input.lower())
        if mode=="Decoder":
            output = leet_decoder(input.lower())
        st.code(output, language="http")


   
st.divider()


# MORSE GENERATOR
def morse_generator(message): 
    MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',  'c':'-.-.', 'd':'-..', 'e':'.',  'f':'..-.', 'g':'--.', 'h':'....',  'i':'..', 'j':'.---', 'k':'-.-',  'l':'.-..', 'm':'--', 'n':'-.',  'o':'---', 'p':'.--.', 'q':'--.-',  'r':'.-.', 's':'...', 't':'-',  'u':'..-', 'v':'...-', 'w':'.--',  'x':'-..-', 'y':'-.--', 'z':'--..',  '1':'.----', '2':'..---', '3':'...--',  '4':'....-', '5':'.....', '6':'-....',  '7':'--...', '8':'---..', '9':'----.',  '0':'-----', ', ':'--..--', '.':'.-.-.-',  '?':'..--..', '/':'-..-.', '-':'-....-',  '(':'-.--.', ')':'-.--.-'} 
    morse_code = '' 
    for letter in message: 
        if letter != ' ': 
            if letter not in MORSE_CODE_DICT:
                pass
            else:
                morse_code += MORSE_CODE_DICT[letter] + ' '
        else: 
            morse_code += ' '
    return morse_code 

# USER INTERFACE
with st.form("Morse"):
    st.header("Morse Code Generator")
    input = st.text_input("Input", value="")
    if st.form_submit_button("Submit", use_container_width=True):
        output = morse_generator(input.lower())
        st.code(output, language="http")


   
st.divider()

st.warning("> ### *More Tools Coming Soon...*")
