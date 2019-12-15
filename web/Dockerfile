FROM nginx

ARG version=1.1

RUN apt-get update && \
    apt-get install -y wget curl vim git

WORKDIR /home/

RUN wget https://github.com/patklaey/ZermattReservationWebClient/archive/v${version}.tar.gz

RUN tar -zxf v${version}.tar.gz

RUN cp -r ZermattReservationWebClient-${version}/* /usr/share/nginx/html
