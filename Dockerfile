FROM python:3.8-alpine

LABEL "project"="tests suggested from selenium and pytest"

WORKDIR ./app

COPY . .

RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/*

