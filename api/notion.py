import httpx


class Notion:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Conteint-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def list_entities(self):
        url = self.base_url + "search"
        r = httpx.post(url, headers=self.headers)

        return r.json()


if __name__ == "__main__":
    from decouple import config

    notion = Notion("https://api.notion.com/v1/", config("NOTION_API_KEY"))
    entities = notion.list_entities()
    for result in entities["results"]:
        print(result["object"])
        print(result["id"])
        if result.get("title"):
            print(result["title"])
        print("===============================")
