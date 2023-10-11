from repositories import SecretRepository

import streamlit as st


secret_repository = SecretRepository()


def on_click():
    secret_repository.save_secret()


def guide_page_component(secret_key, data):
    st.title("Configure Notion API integration settings.")

    if secret_key:
        st.markdown("### List of Notion Pages")
        st.dataframe(data)
    else:
        st.markdown("### Internal Integration Secret")
        f = st.form("integration")
        f.text_input("Integration Secret", type="password", key="secret_key")
        f.form_submit_button("Connect", on_click=on_click)
