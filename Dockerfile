FROM ubuntu:16.04
MAINTAINER Haoji Liu

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list

RUN apt-get -y update
RUN apt-get install -y build-essential nginx git curl wget python-setuptools python-dev python-pip python2.7 supervisor

# TODO: Use volume
RUN mkdir /srv/logs

ADD ./app /srv/app

EXPOSE 80 443

# Copy config files over
COPY ./config/supervisord.conf /etc/supervisord.conf
COPY ./config/nginx.conf /etc/nginx/sites-available/app

# Check nginx config
# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
RUN nginx -t

ADD ./config /srv/config
RUN pip install --upgrade pip
RUN pip install -r /srv/config/requirements.txt

# Unit test
# WORKDIR /srv/app/src/py/tests
# RUN pytest

# Start supervisord
WORKDIR /srv/app
CMD ["/usr/bin/supervisord"]
