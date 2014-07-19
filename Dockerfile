from ubuntu:12.04

maintainer Felipe Arruda "contato@arruda.blog.br"

RUN apt-get -qq -y update

RUN apt-get install -y build-essential git-core
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y nginx supervisor
RUN apt-get install -y python-pip


# install nginx
RUN apt-get install -y python-software-properties
RUN apt-get update
RUN add-apt-repository -y ppa:nginx/stable

#Postgres deps
RUN apt-get install -y libpq-dev

ADD . /home/docker/proj/

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /home/docker/proj/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /home/docker/proj/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
RUN pip install -r /home/docker/proj/requirements/docker.txt

ENV ENV_SETTINGS docker

expose 80
cmd /bin/bash /home/docker/proj/prepare_server.sh