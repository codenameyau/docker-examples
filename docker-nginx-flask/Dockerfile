FROM ubuntu:14.04
MAINTAINER Jorge Yau "codenameyau@gmail.com"

# Copy files.
ADD . /srv

# Install packages.
RUN apt-get -y update && install
  python \
  python-dev \
  python-pip \
  nginx
RUN pip install -r /srv/requirements/prod.txt

# Setup nginx with uWSGI.
RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log
ADD ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
