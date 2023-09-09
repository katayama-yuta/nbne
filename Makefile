format:
	poetry run black /app/src/

lint:
	poetry run ruff check /app/src/