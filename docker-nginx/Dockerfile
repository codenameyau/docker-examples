FROM nginx

RUN mkdir /etc/nginx/logs && touch /etc/nginx/logs/static.log

ADD .docker/nginx.conf /etc/nginx/conf.d/default.conf
ADD app /www
