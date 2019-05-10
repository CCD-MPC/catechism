FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
	&& apt-get -y install git \
	&& apt-cache show python3 \
	&& apt-get -y install python3=3.5.1* \
	&& apt-get install -y python3-pip

RUN cd /app \
	&& git clone https://github.com/cici-conclave/conclave.git \
	&& cd /app/conclave \
	&& pip3 install -r requirements.txt \
	&& pip3 install -e git+https://github.com/IQSS/dataverse-client-python.git#egg=dataverse \
	&& python3.5 setup.py develop

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
