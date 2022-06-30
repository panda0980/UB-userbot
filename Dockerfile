FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y

RUN git clone https://github.com/panda0980/UB-userbot.git /root/ub

WORKDIR /root/ub

RUN pip3 install -U -r requirements.txt
