FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY ./web/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

CMD /usr/local/bin/gunicorn -w 2 -b :8000 app:app --reload
