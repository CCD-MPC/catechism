FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get -y install git \
    && apt-cache show python3 \
    && apt-get -y install python3=3.5.1* \
    && apt-get install -y python3-pip \
    && apt-get install -y iputils-ping \
    && apt-get install -y nmap

RUN cd /app \
    && git clone https://github.com/cici-conclave/conclave-web.git 

RUN cd /app/conclave-web \
    && pip3 install -r requirements.txt

RUN mkdir /etc/swift-config/

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
    && chmod -R 777 /app \
    && chmod +x /app/start.sh

USER appuser

CMD "./start.sh"