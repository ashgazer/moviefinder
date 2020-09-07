
enviro:
	source ./venv/bin/activate

setup:
	python -m venv venv

install: setup enviro
	pip install -r requirements.txt

test:
	pytest

clean:
	rm -r venv