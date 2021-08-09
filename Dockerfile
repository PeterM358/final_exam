COPY ./store_app myproject

WORKDIR /store_app

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]