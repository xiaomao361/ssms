FROM python:3.9

LABEL MAINTAINER="zhouwei" email='xiaomao361@163.com'

WORKDIR /home

RUN apt-get update
RUN apt-get -y install zip ansible dos2unix git
RUN git clone git@github.com:xiaomao361/ssms.git
RUN mv /home/ssms/docker/entrypoint.sh /usr/bin/entrypoint.sh

EXPOSE 8000

CMD ["entrypoint.sh"]