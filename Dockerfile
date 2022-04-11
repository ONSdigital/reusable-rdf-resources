FROM python:3.10

RUN apt-get update
RUN apt-get install -y git 

RUN python3 -m pip install poetry

RUN mkdir /workspaces
WORKDIR /workspaces