FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt
RUN python3 -m spacy download en_core_web_md

RUN mkdir /app
WORKDIR /app
COPY ./app /app
