DOCKER_CMD ?= docker # Swap for nerdctl if using containerd

default: build
	$(DOCKER_CMD) run --rm -t -v `pwd`:/opt/dmsc_code_challenge dmsc_code_challenge:latest

build:
	$(DOCKER_CMD) build -t dmsc_code_challenge:latest .

lint: build
	$(DOCKER_CMD) run --rm -t -v `pwd`:/opt/dmsc_code_challenge dmsc_code_challenge:latest poetry run pylint *.py test/

test: build
	$(DOCKER_CMD) run --rm -t -v `pwd`:/opt/dmsc_code_challenge dmsc_code_challenge:latest poetry run pytest

requirements.txt:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: default build lint test
