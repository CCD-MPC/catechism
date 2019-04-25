FROM ubuntu:16.04

WORKDIR /app

COPY . /app

RUN apt-get update \
	&& apt-get -qq -y install curl

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get -y install nodejs \
	&& apt-get -y install git

RUN cd /app \
    && git clone https://github.com/multiparty/jiff.git \
    && cd /app/jiff \
    && npm install \
    && npm install express

RUN groupadd -g 666 appuser \
	&& useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app

USER appuser

CMD ["bash", "run.sh"]