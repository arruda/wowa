#!/bin/bash

echo "waitig for DB"
while ! exec 6<>/dev/tcp/${DB_PORT_5432_TCP_ADDR}/${DB_PORT_5432_TCP_PORT}; do
    echo "$(date) - still trying to connect to db at ${DB_PORT}"
    sleep 1
done

# Syncdb and collect statics
python /home/docker/proj/wowa/manage.py syncdb --noinput
#python /home/docker/proj/wowa/manage.py loaddata /home/docker/proj/wowa/wowa/fixtures/admin_user.yaml
python /home/docker/proj/wowa/manage.py collectstatic --noinput

/bin/bash /home/docker/proj/gunicorn_start.sh