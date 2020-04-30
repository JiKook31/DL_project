FROM python:3.6-stretch
COPY . predictbot
WORKDIR predictbot

RUN python3.6 -m pip install -r requirements.txt
RUN python3.6 -m pip install --no-cache-dir install torch
RUN python3.6 -m pip install sacremoses subword_nmt
CMD python3.6 serverbot.py

