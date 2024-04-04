pip-tools:
	pip install pip-tools>=7.0.0 setuptools>=68.0.0

pip-tools-dev:
	pip-compile requirements/dev.in
	pip-sync requirements/dev.txt

lint:
	ruff . --fix
	mypy .