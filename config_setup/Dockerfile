FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
	&& apt-get -y install git \
	&& apt-cache show python3 \
	&& apt-get -y install python3=3.5.1* \
	&& apt-get install -y python3-pip

RUN cd /app \
	&& git clone https://github.com/cici-conclave/config_setup.git \
	&& cd /app/config_setup \
	&& pip3 install -r requirements.txt \
	&& python3.5 setup.py develop

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app \
	&& chmod +x /app/run.sh

RUN mkdir /etc/protocol_config

RUN chmod -R 777 /etc/protocol_config

USER appuser

CMD ["bash", "run.sh"]