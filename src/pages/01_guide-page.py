import streamlit as st
from api.notion import NotionClient
import time
import pandas as pd

st.title("Configure Notion API integration settings.")

with st.form("my_form"):
    st.markdown("### Internal Integration Secret")
    secret_key = st.text_input("Integration Secret")
    submitted = st.form_submit_button("連携")

# submittedが実行された時の処理
if submitted:
    with st.spinner("Notionと連携中..."):
        time.sleep(3)
    notion_client = NotionClient(secret_key)
    pages = notion_client.list_entities().get("results")

    page_title = []
    page_url = []
    page_id = []

    for p in [i["properties"] for i in pages]:
        if p.get("title") is not None:
            # st.markdown(type(p))
            # st.markdown(p)

            # st.markdown(type(p.get("title")))
            # st.markdown(p.get("title"))

            # st.markdown(type(p.get("title").get("title")))
            # st.markdown(p.get("title").get("title"))

            title_info = p.get("title").get("title")
            page_title.append([i["text"]["content"] for i in title_info])

    page_url = [i["url"] for i in pages]
    page_id = [i["id"] for i in pages]

    st.markdown(page_title)
    st.markdown(page_url)
    st.markdown(page_id)

    df = pd.DataFrame(
        zip(page_title, page_url, page_id), columns=["title", "URL", "database_id"]
    )
    st.markdown("### List of Notion Pages")
    st.dataframe(df)
