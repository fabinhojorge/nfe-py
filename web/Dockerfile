FROM python:3

RUN mkdir /app
WORKDIR /app/web
COPY requirements.txt /app/web/requirements.txt
RUN python -m pip install -r requirements.txt
