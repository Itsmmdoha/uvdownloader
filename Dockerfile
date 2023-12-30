FROM python:latest

COPY . /uvdownloader

WORKDIR /uvdownloader

RUN pip install -r requirements.txt

CMD ["gunicorn","-b","0.0.0.0:8000","app:app"]

EXPOSE 8000
