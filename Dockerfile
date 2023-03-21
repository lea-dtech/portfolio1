FROM python:3.9.6-alpine AS builder

WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /django

EXPOSE 8000

CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py", "runserver","0.0.0.0:8000"]
