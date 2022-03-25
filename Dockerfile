FROM python:3.9

LABEL MAINTAINER="zhouwei" email='xiaomao361@163.com'

WORKDIR /home

ADD ./* /home/
RUN apt-get update 
RUN apt-get -y install ansible dos2unix
RUN pip install -r requirements.txt

ADD entrypoint.sh /usr/bin/entrypoint.sh

EXPOSE 8000

CMD ["entrypoint.sh"]