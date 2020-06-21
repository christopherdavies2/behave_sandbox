FROM python:3.6-slim-stretch
COPY . /
RUN apt-get update \
    && apt-get install -y python3-dev python3-pip \
    && pip3 install behave \
    && pip install requests