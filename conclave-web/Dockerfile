FROM rhel7

WORKDIR /app

COPY . /app

RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -

RUN yum -y update \
    && yum -y install git \
    && yum -y install nodejs \
    && yum -y install wget

RUN wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm -ivh /app/epel-release-latest-7.noarch.rpm

RUN yum -y install epel-release \
    && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python35u python35u-pip


RUN pip3.5 install virtualenv

RUN cd /app \
    && git clone https://github.com/cici-conclave/conclave-web.git \
    && virtualenv backend/venv \
    && source backend/venv/bin/activate

RUN cd /app/conclave-web \
    && pip3.5 install -r requirements.txt

RUN cd /app/conclave-web/frontend \
    && npm install \
    && npm run build

RUN groupadd -g 666 appuser && \
     useradd -r -u 666 -g appuser appuser

RUN chown appuser:appuser -R /app \
	&& chmod -R 777 /app \
	&& chmod +x /app/start.sh

USER appuser

CMD "./start.sh"