FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get -y install git \
    && apt-get install -y iputils-ping \
    && apt-get install -y nmap

RUN cd /app \
    && git clone https://github.com/CCD-MPC/chamberlain.git

RUN cd /app/chamberlain \
    && pip install -r requirements.txt

RUN mkdir /etc/swift-config/

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
    && chmod -R 777 /app \
    && chmod +x /app/start.sh

USER appuser

CMD "./start.sh"
