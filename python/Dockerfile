FROM python:3.8.6-slim
COPY . /app
RUN apt-get update && apt-get install gcc -y && apt-get clean
WORKDIR /app
RUN pip install pip setuptools --upgrade && pip install -r requirements.txt
CMD python /app/example.py
