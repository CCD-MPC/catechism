FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get -y install git 

RUN cd /app \
	&& git clone https://github.com/cici-conclave/provenance.git \
	&& cd /app/provenance \
	&& pip install -r requirements.txt \
	&& pip install -e git+https://github.com/IQSS/dataverse-client-python.git#egg=dataverse \
	&& python setup.py develop

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app \
	&& chmod +x /app/run.sh

USER appuser

CMD "./run.sh"