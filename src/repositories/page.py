import pandas as pd


class PageRepository:
    def __init__(self, notion_client):
        self.notion_client = notion_client

    def load_pages(self):
        pages = self.notion_client.list_entities().get("results")
        page_title = []
        page_url = []
        page_id = []

        for p in [i["properties"] for i in pages]:
            if p.get("title") is not None:
                title_info = p.get("title").get("title")
                page_title.append([i["text"]["content"] for i in title_info])

        page_url = [i["url"] for i in pages]
        page_id = [i["id"] for i in pages]
        df = pd.DataFrame(
            zip(page_title, page_url, page_id), columns=["title", "URL", "database_id"]
        )
        return df
