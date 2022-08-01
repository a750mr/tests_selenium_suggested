FROM python:3.9-slim

LABEL "project"="tests suggested from selenium and pytest"

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR ./app

COPY . .

RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/* --headless


