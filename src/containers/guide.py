from repositories import PageRepository, SecretRepository
from apis.notion import NotionClient
from components import guide_page_component


def guide_page_container():
    secret_key = SecretRepository().load_secret()
    notion_client = NotionClient(secret_key)
    page_repository = PageRepository(notion_client)

    if secret_key:
        pages = page_repository.load_pages()
        guide_page_component(pages)
    else:
        guide_page_component(None)
