FROM python:3.9-alpine3.15

ENV PYTHONBUFFERED=1

WORKDIR /Lemall

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn lemall.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
