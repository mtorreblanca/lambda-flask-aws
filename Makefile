install:
	python3 -m venv venv
activate:
	. venv/bin/activate
requirements:
	pip freeze > requirements.txt
requirements-install:
	pip install -r requirements.txt