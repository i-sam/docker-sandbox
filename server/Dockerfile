############################################################
# Dockerfile to build simple Python Application server based on flask
# Based on Ubuntu image
############################################################

FROM ubuntu

MAINTAINER Sam Bukreev

RUN apt-get update && apt-get install -y apt-utils python python-dev python-distribute python-pip

ADD . /server

RUN pip install --upgrade pip && pip install -r /server/requirements.txt

EXPOSE 80

WORKDIR /server

CMD python server.py
