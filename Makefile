.PHONY devenv-create:
devenv-create:
	virtualenv devenv

.PHONY devenv:
devenv:
	@echo "Run 'source ./devenv/bin/activate' to activate your virtual environment."

.PHONY deps:
deps:
	pip install -r requirements.txt

.PHONY test:
test:
	pytest

