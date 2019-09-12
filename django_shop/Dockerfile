FROM python:3.6

ENV PYTHONUNBUFFERED=1
ENV APP_DIR=/django_shop

RUN mkdir -p /var/log/gunicorn

RUN mkdir $APP_DIR

WORKDIR $APP_DIR
ADD requirements.txt $APP_DIR/
RUN pip install -r requirements.txt

ADD . $APP_DIR/