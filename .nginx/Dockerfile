#
# Nginx Dockerfile
#
# https://github.com/dockerfile/nginx
#

# Pull base image.
FROM ubuntu:12.04

RUN apt-get -qq -y update

RUN apt-get install -y build-essential
RUN apt-get install -y python-software-properties


# Install Nginx.
RUN add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
VOLUME ["/data/static","/data/media","/etc/nginx/sites-enabled", "/var/log/nginx"]

RUN rm /etc/nginx/sites-enabled/default

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443