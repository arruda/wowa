from ubuntu:12.04

maintainer Felipe Arruda "contato@arruda.blog.br"

run apt-get -qq -y update

run apt-get install -y build-essential git-core
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run easy_install pip

# install nginx
run apt-get install -y python-software-properties
run apt-get update
RUN add-apt-repository -y ppa:nginx/stable

add . /home/docker/proj/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/proj/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/proj/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /home/docker/proj/requirements/docker.txt

expose 80
# cmd ["supervisord", "-n"]
