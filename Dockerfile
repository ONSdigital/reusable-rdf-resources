FROM python:3.10-buster

RUN apt-get update && apt-get install -y git 

RUN python3 -m pip install poetry

COPY scripts/pyproject.toml /
COPY scripts/poetry.lock /

RUN poetry export --format requirements.txt --output requirements.txt --without-hashes --dev
# Install all dependencies listed in text file to the test environment.
RUN pip install --requirement requirements.txt

RUN rm requirements.txt /pyproject.toml /poetry.lock

RUN mkdir /workspaces
WORKDIR /workspaces