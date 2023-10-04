import streamlit as st
from api.notion import NotionClient

st.title("This is guide page")
secret_key = st.text_input("Please enter your notion URL")


## store credential in .nbne
