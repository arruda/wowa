#!/bin/bash

NAME="wowa"                                  # Name of the application
DJANGODIR=/home/docker/proj/wowa             # Django project directory
SOCKFILE=/home/docker/proj/run/gunicorn.sock  # we will communicte using this unix socket
#USER=hello                                        # the user to run as
#GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=wowa.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=wowa.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug
# \
#  --user=$USER --group=$GROUP \
#  --bind=unix:$SOCKFILE