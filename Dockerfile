FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install Flask gunicorn

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5011"]
