COPY requirements.txt /store_app/requirements.txt

COPY . /store_app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]