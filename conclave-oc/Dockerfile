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

RUN apt-get -y install ocaml libgcrypt20-dev \
	&& apt-get -y install ocaml-findlib opam m4

RUN opam init \
	&& opam switch 4.06.0 \
	&& eval 'opam config env' \
	&& opam install camlp4 ocamlfind ocamlbuild batteries

RUN git clone https://github.com/samee/obliv-c.git \
	&& cd obliv-c \
	&& ./configure && make

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app \
	&& chmod +x /app/run.sh

USER appuser

CMD "./run.sh"
