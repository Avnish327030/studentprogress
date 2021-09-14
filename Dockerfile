FROM python:3

ENV PYTHONUNBUFFERED 1

ARG AWS_ACCESS_KEY_ID

ARG AWS_SECRET_ACCESS_KEY

ARG AWS_DEFAULT_REGION
ARG DJANGO_ALLOWED_HOSTS
ARG SECRET_KEY
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV SECRET_KEY $SECRET_KEY
WORKDIR /app

ADD . /app


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python","manage.py","runserver","0.0.0.0:5000"]



