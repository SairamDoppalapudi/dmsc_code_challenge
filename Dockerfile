FROM public.ecr.aws/docker/library/python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    WORKDIR=/opt/dmsc_code_challenge

RUN mkdir -p $POETRY_HOME && \
    mkdir -p $WORKDIR &&\
    pip install poetry

WORKDIR $WORKDIR
COPY pyproject.toml .
RUN poetry install
COPY . .
CMD poetry run pylint validate_metadata.py test/ && poetry run pytest
