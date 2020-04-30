FROM python:3.7-alpine
COPY . predictbot
WORKDIR predictbot

RUN python3.7 -m pip install -r requirements.txt
CMD python3.7 serverbot.py

