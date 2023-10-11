import streamlit as st


class SecretRepository:
    def __init__(self):
        pass

    @staticmethod
    def save_secret():
        print("Save secret: ", st.session_state.secret_key)

    @staticmethod
    def load_secret():
        print("Loading secret...")
        if "secret_key" not in st.session_state:
            return None

        return st.session_state.secret_key
