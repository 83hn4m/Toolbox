# STREAMLIT
import streamlit as st

# --- PAGE CONFIG (BROWSER TAB) ---
st.set_page_config(page_title="Toolbox", page_icon=":toolbox:", layout="centered", initial_sidebar_state="expanded")

# --- MAIN PAGE ---
with st.container():
        st.title("🧰 Toolbox")
        st.info("I keep my tools here, feel free to use!")