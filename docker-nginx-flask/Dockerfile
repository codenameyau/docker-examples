FROM ubuntu:14.04
MAINTAINER Jorge Yau "codenameyau@gmail.com"

# Copy app files to '/srv' directory.
ADD . /srv

# Install ubuntu packages.
RUN apt-get -y update
RUN apt-get -y install \
  python3-pip \
  python3-dev \
  nginx

# Install pip packages.
RUN pip3 install -r /srv/requirements.txt

# Setup uWSGI.
ADD ./deployment/application.conf /etc/init/application.conf

# Setup nginx.
RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log
ADD ./deployment/nginx.conf /etc/nginx/conf.d/default.conf
