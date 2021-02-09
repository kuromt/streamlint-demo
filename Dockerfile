FROM python:3.9

COPY apps/ /root/
WORKDIR /root

RUN apt update -y && \
    apt install vim -y 

RUN pip install -r requirement.txt