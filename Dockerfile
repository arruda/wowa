from ubuntu:12.04

maintainer Felipe Arruda "contato@arruda.blog.br"

RUN apt-get -qq -y update

RUN apt-get install -y build-essential git-core
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y python-pip

#Postgres deps
RUN apt-get install -y libpq-dev

ADD . /home/docker/proj/

# run pip install
RUN pip install -r /home/docker/proj/requirements/docker.txt

ENV ENV_SETTINGS docker

expose 8000
cmd /bin/bash /home/docker/proj/prepare_server.sh