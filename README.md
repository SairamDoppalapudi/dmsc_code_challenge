DMSC Code Challenge
===================

This repo contains a simplified version of a real-world project from a SPE DMSC
initiative.  Review the [Sample Story](/sample_story.md) for a full
description of the requirements.

You don't have to achieve all of the acceptance criteria. While that is the
goal, It's better that you write high-quality code that fulfills one
requirement than low-quality code trying to cram all requirements in in the
given time.

**Adding comments to illustrate your thought process is highly encouraged.**

## Setup

1. Fork this repository.
2. `git clone` your fork.
3. Initialize project.  There are several ways to do this provided:
  - `poetry`: Use the Python Poetry package manager to install dependencies into
    a virtualenv
  - Docker / Containerd: Build a container with the `Dockerfile` and run linting
    and tests in the container.  This is automated though the included
    `Makefile`... just run `make` to build the container and run linting / tests
  - `pip`: Use the included `requirements.txt` to install dependencies to your
    system, sans virtualenv.  `pip install [--user] -r requirements.txt`

## Tests / Linting

A test file for `validate_metadata.py` is provided.  The goal of this code
challenge is to make these tests pass.  For code quality and consistency, the
linter should also run without warnings.

### To lint:
  - via `poetry`: `poetry run pylint *.py`
  - via Docker: ``docker run --rm -t -v `pwd`:/opt/dmsc_code_challenge dmsc_code_challenge:latest poetry run pylint *.py``
    (also via `make lint`)
  - via `pip`: `pylint *.py`

### To test:
  - via `poetry`: `poetry run pytestt`
  - via Docker: ``docker run --rm -t -v `pwd`:/opt/dmsc_code_challenge dmsc_code_challenge:latest poetry run pytest``
    (also via `make test`)
  - via `pip`: `pytest`

## Wrapping up

When you have completed coding, commit and push to your fork and open a PR
against the upstream repo so we can review your work.

---

## Resources

This challenge uses the following tools / modules, documented here for your
reference:

- [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader)
- [poetry](https://python-poetry.org/)
- [pylint](https://pylint.pycqa.org/en/latest/index.html)
- [pytest](https://docs.pytest.org/en/6.2.x/index.html)
