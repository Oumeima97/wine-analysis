FROM python:3

WORKDIR /app

COPY ./src/process/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src/process /app

COPY ./database.env /app

COPY ./data /app/data

COPY ./wait-for-it.sh /app/wait-for-it.sh