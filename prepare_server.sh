#!/bin/bash

# Syncdb and collect statics
python /home/docker/proj/wowa/manage.py syncdb --noinput
python /home/docker/proj/wowa/manage.py loaddata /home/docker/proj/wowa/wowa/fixtures/admin_user.yaml
python /home/docker/proj/wowa/manage.py collectstatic --noinput

supervisord -n