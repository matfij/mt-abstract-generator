FROM python:3.7

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser runuser
USER runuser
