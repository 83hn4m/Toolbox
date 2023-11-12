# STREAMLIT
import streamlit as st

# --- PAGE CONFIG (BROWSER TAB) ---
st.set_page_config(page_title="Toolbox", page_icon=":toolbox:", layout="centered", initial_sidebar_state="expanded")

# --- MAIN PAGE ---
with st.container():
        st.title("🧰 Toolbox")
        st.markdown("""
                    #### *I'm just keeping my tools here, feel free to use and share.*
                    This app is going to be hosted in your own system, so the cache will be cleared every time you refresh the page.
                    So your data and privacy is safe.
                    """)
        st.divider()
        st.header("♺ Updates - v0.0.1")
        st.success("""Text tools added with **3** tools:
                   \n - Password Generator
                   \n - Leet Code
                   \n - Morse Code
                   """)
        st.divider()

        