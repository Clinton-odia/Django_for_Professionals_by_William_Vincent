FROM python:3.12-alpine

#set environment variable
 ENV PYTHONUNBUFFERED=1
 ENV PYTHONDONTWRITEBYTECODE=1

 #set working dir
 WORKDIR /code/

 #install dependencies

 COPY Pipfile Pipfile.lock /code/
 RUN pip install pipenv && pipenv install --system

 #copy project
 COPY . /code/