FROM ubuntu:latest
LABEL maintainer="pat@247.ch"

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev git curl vim

COPY requirements.txt /home/html/

RUN pip3 install -r /home/html/requirements.txt

WORKDIR /home/html

RUN git clone https://github.com/patklaey/ZermattReservationAPI/

WORKDIR /home/html/ZermattReservationAPI

COPY ./uwsgi.ini /home/html/ZermattReservationAPI/
RUN mkdir -p /var/log/uwsgi/ 

#CMD uwsgi --ini /home/html/ZermattReservationAPI/uwsgi.ini
CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --uid www-data --gid www-data --enable-threads -w main:app 

EXPOSE 5000
