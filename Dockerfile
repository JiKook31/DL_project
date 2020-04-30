FROM python:3.6-stretch
COPY . predictbot
WORKDIR predictbot

RUN python3.6 -m pip install -r requirements.txt
CMD python3.6 serverbot.py

