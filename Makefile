


setup:
	python -m venv venv

requirements:
	pip install -r requirements.txt

test:
	pytest ./tests