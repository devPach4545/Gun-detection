FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r /app/requirements.txt

CMD [ "python3", "app.py" ]