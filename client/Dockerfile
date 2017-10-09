############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

FROM ubuntu

MAINTAINER Sam Bukreev

RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip

ADD . /client

RUN pip install --upgrade pip && pip install -r /client/requirements.txt

WORKDIR /client

CMD python client.py
