FROM python:slim-bullseye

WORKDIR /work

COPY ./ ./

RUN pip install -r requirements.txt
