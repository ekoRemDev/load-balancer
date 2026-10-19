from python:3.12.0-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
