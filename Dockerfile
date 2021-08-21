FROM python:3.9


# Set work directory
WORKDIR /code
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1


COPY . /code/

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
#FROM python:3
#ENV PYTHONUNBUFFERED=1
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/
#CMD ["python3", "manage.py", "runserver"]


