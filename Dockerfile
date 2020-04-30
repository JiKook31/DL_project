FROM python:3.6-stretch
COPY . predictbot
WORKDIR predictbot

RUN python3.6 -m pip install -r requirements.txt
#RUN python3.6 -m pip install http://download.pytorch.org/whl/cpu/torch-0.3.1-cp36-cp36m-linux_x86_64.whl
RUN python3.6 -m pip install torch
RUN python3.6 -m pip --no-cache-dir install torchvision
RUN python3.6 -m pip install sacremoses subword_nmt
CMD python3.6 serverbot.py

