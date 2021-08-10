#COPY ./store_app /store_app
#
#WORKDIR /store_app
#
#RUN pip install -r requirements.txt
#
#RUN python manage.py migrate
#
#CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

#FROM python:3.8
#
#ENV PYTHONUNBUFFERED 1
#ENV WORKDIR /usr/src/app
#
#WORKDIR ${WORKDIR}
#
#RUN pip install --upgrade pip && pip install pipenv
#
#COPY ./* ${WORKDIR}/
#
#RUN pipenv lock --requirements > requirements.txt
#
#RUN pip install -r requirements.txt
#
#ADD . ${WORKDIR}/


# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/