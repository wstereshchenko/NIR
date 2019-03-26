FROM python:3.7

ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /home/project/

COPY Project_1 /home/project
WORKDIR /home/project

RUN pip install -r requirements.txt