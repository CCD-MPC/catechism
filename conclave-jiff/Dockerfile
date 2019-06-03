FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get -qq -y install curl

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get update \
    && apt-get -y install git \
    && apt-cache show python3 \
    && apt-get -y install python3=3.5.1* \
    && apt-get install -y python3-pip \
    && apt-get install -y nodejs

RUN cd /app \
    && git clone https://github.com/cici-conclave/conclave.git \
    && cd /app/conclave \
    && pip3 install -r requirements.txt \
    && python3.5 setup.py develop

RUN cd /app \
    && git clone https://github.com/cici-conclave/conclave_data.git \
    && cd /app/conclave_data \
    && pip3 install -r requirements.txt \
    && pip3 install -e git+https://github.com/IQSS/dataverse-client-python.git#egg=dataverse \
    && python3.5 setup.py develop

RUN cd /app \
    && git clone https://github.com/multiparty/jiff.git \
    && cd /app/jiff \
    && npm install

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app \
	&& chmod +x /app/run.sh

USER appuser

CMD "./run.sh"