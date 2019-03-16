FROM rhel7

WORKDIR /app

COPY . /app

RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -

RUN yum -y update \
    && yum -y install git \
    && yum -y install wget \
    && yum -y install nodejs

RUN wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm -ivh /app/epel-release-latest-7.noarch.rpm

RUN yum -y install epel-release \
    && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python35u python35u-pip

RUN rm -r /app/epel-release-latest-7.noarch.rpm -f

RUN cd /app \
	&& git clone https://github.com/cici-conclave/conclave.git \
	&& cd /app/conclave \
	&& pip3.5 install -r requirements.txt \
	&& pip3.5 install -e git+https://github.com/IQSS/dataverse-client-python.git#egg=dataverse \
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