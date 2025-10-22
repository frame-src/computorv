IMAGE_NAME = computorv1

CURRENT_DIR = $(shell pwd)

all: install

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -v $(CURRENT_DIR)/app:/usr/src -it $(IMAGE_NAME)

clean:
	docker image rm $(IMAGE_NAME)

test:
	# pytest -v --maxfail=1 --disable-warnings -q
	pytest -v -s 

lint:
	ruff check app tests

venv:
	python3 -m venv venv
	@echo "Virtual environment created. Activate it with: source venv/bin/activate"

install: venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r test_requirements.txt

.PHONY: build run