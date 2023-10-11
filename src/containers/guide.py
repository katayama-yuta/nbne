from repositories import PageRepository, SecretRepository
from apis.notion import NotionClient
from components import guide_page_component

secret_repository = SecretRepository()
notion_client = NotionClient(secret_repository.load_secret())
page_repository = PageRepository(notion_client)


def guide_page_container():
    secret_key = secret_repository.load_secret()
    if secret_key:
        data = page_repository.load_pages()
        guide_page_component(secret_key, data)
    else:
        guide_page_component(None, None)
