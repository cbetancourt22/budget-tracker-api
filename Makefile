VENV_NAME := venv
PYTHON := python3
PIP := $(VENV_NAME)/bin/pip
PYTHON_UVICORN := $(VENV_NAME)/bin/python
PYTHON_BLACK := $(VENV_NAME)/bin/python

ifeq ($(OS),Windows_NT)
    PIP := $(VENV_NAME)/Scripts/pip.exe
    PYTHON_UVICORN := $(VENV_NAME)/Scripts/python.exe
    PYTHON_BLACK := $(VENV_NAME)/Scripts/python.exe
endif

HOST := 127.0.0.1
PORT := 8000
SWAGGER_URL := http://$(HOST):$(PORT)/docs

unameOut := $(shell uname)

# Determine how to open Swagger UI depending on OS
ifeq ($(OS),Windows_NT)
OPEN_CMD := start "" $(SWAGGER_URL)
else
ifeq ($(unameOut),Darwin)
OPEN_CMD := open $(SWAGGER_URL)
else
OPEN_CMD := xdg-open $(SWAGGER_URL) || true
endif
endif

.PHONY: all install run clean format

all: run

format:
	@echo "Formatting Python files with Black..."
	$(PYTHON_BLACK) -m black app

install:
	@if [ ! -d "$(VENV_NAME)" ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv --copies $(VENV_NAME); \
	fi
	@echo "Installing dependencies inside venv..."
	$(PIP) install -r requirements.txt
	$(PIP) install uvicorn[standard]

run: install
	@echo "Running FastAPI server at $(SWAGGER_URL)..."
	@$(OPEN_CMD)
	$(PYTHON_UVICORN) -m uvicorn app.main:app --host $(HOST) --port $(PORT) --reload

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_NAME)
