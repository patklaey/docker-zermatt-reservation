FROM ubuntu:latest
LABEL maintainer="pat@247.ch"

ARG version=1.0

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev wget curl vim

COPY requirements.txt /home/html/

RUN pip3 install -r /home/html/requirements.txt

# Set the locale
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/html

RUN wget https://github.com/patklaey/ZermattReservationAPI/archive/v${version}.tar.gz
RUN tar -zxf v${version}.tar.gz
RUN mv ZermattReservationAPI-${version} ZermattReservationAPI

WORKDIR /home/html/ZermattReservationAPI

COPY ./uwsgi.ini /home/html/ZermattReservationAPI/
RUN mkdir -p /var/log/uwsgi/ 

CMD uwsgi --ini /home/html/ZermattReservationAPI/uwsgi.ini

EXPOSE 5000
