#FROM python:3.7-alpine
FROM python:3.7

ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /home/project/

COPY Project_1 /home/project
WORKDIR /home/project

#RUN python setup.py build_ext --pg-config postgresql/pg.conf build/
RUN pip install -r requirements.txt