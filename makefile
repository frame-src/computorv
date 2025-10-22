IMAGE_NAME = computorv1

CURRENT_DIR = $(shell pwd)

all: build run

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
	ruff check computor tests

.PHONY: build run