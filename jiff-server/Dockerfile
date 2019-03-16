FROM rhel7

WORKDIR /app

COPY . /app

RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -

RUN yum -y update \
    && yum -y install git \
    && yum -y install nodejs

RUN cd /app \
    && git clone https://github.com/multiparty/jiff.git \
    && cd /app/jiff \
    && npm install \
    && npm install express

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app

USER appuser

CMD ["bash", "run.sh"]