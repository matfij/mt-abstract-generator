FROM python:3.7-alpine

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D runuser
USER runuser
