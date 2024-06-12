.DEFAULT_GOAL := help

SHELL=/bin/bash
VENV = venv

# Detect the operating system and set the virtualenv bin directory
ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif

setup: $(VENV)/bin/activate

$(VENV)/bin/activate: $(VENV)/.venv-timestamp

$(VENV)/.venv-timestamp: src/dbgpt-hub-nlu/setup.py requirements
	# Create new virtual environment if setup.py has changed
	python3 -m venv $(VENV)
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install -r requirements/lint-requirements.txt
	touch $(VENV)/.venv-timestamp


.PHONY: fmt
fmt: setup ## Format Python code
	# TODO: Use isort to sort Python imports.
	# https://github.com/PyCQA/isort
	$(VENV_BIN)/isort src/
	# https://github.com/psf/black
	$(VENV_BIN)/black --extend-exclude="examples/notebook" .