FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get -qq -y install curl

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get -y install git \
    && apt-get install -y nodejs \
    && apt-get install -y iputils-ping \
    && apt-get install -y nmap

RUN cd /app \
    && git clone https://github.com/multiparty/conclave.git \
    && cd /app/conclave \
    && pip install -r requirements.txt \
    && python setup.py develop

RUN cd /app \
    && git clone https://github.com/CCD-MPC/curia.git \
    && cd /app/curia \
    && pip install -r requirements.txt \
    && pip install -e git+https://github.com/IQSS/dataverse-client-python.git#egg=dataverse \
    && python setup.py develop

RUN cd /app \
    && git clone https://github.com/CCD-MPC/dogma.git \
    && cd /app/dogma \
    && pip install -r requirements.txt \
    && python setup.py develop

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