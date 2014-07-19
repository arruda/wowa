#!/bin/bash

NAME="wowa"                                  # Name of the application
DJANGODIR=/home/docker/proj/wowa             # Django project directory
#USER=hello                                        # the user to run as
#GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=wowa.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=wowa.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"
echo $ENV_SETTINGS

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --bind=0.0.0.0:8000
#  --user=$USER --group=$GROUP \