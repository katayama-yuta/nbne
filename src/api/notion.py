import httpx


class NotionClient:
    BASE_URL = "https://api.notion.com/v1"

    def __init__(self, api_key: str):
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Conteint-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def list_entities(self):
        url = f"{self.BASE_URL}/search"
        r = httpx.post(url, headers=self.headers)

        return r.json()


if __name__ == "__main__":
    from decouple import config

    notion = NotionClient(config("NOTION_API_KEY"))
    entities = notion.list_entities()
    for result in entities["results"]:
        print(result["object"])
        print(result["id"])
        if result.get("title"):
            print(result["title"])
        print("===============================")
