format:
	pip install -r requirements/dev-requirements.txt
	black --verbose --config black.toml app
	isort app/**/*.py

run:
	python3 manage.py migrate
	python3 manage.py runserver

migrate:
	python3 manage.py migrate

load_data:
	python3 manage.py loaddata data.json

admin:
	python3 manage.py createsuperuser