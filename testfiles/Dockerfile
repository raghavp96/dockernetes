FROM python:3.5-alpine

RUN pip install flask
COPY flaskapp.py flaskapp.py
ENTRYPOINT ["python", "flaskapp.py"]