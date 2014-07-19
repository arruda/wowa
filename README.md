===================================
wowa
===================================

About this:
-----------------------------------

WOWA is a simple aplication that uses the WOW API to get info about the auction house price for some items.

Runnnig:
--------

Use docker to run this.

So, after installing docker, just use the scripts `build_docker.sh` to build the docker image.
After that run the cmd:

    create_containers.sh

this will create and name the containers, and the app will run in the port 8000.

After this you can use the cmds: `stop_docker.sh` and run `run_docker.sh` to control the containers.

**obs2**: admin user/pass (root/root)

Dockers
-------

There are 3 containers: wowadb, wowaapp and wowanginx.

### wowadb
It uses a PostgreSql docker, that runs on port 5432 (5432 on host)

### wowaapp
A container that runs the app with gunicorn on port 8000 (8001 on host)
It is linked to wowadb to accesses the DB.

Volume:

./ -> /home/docker/proj

###wowanginx
A container that runs nginx on port 80 (8000 on host) and is linked to wowaapp to proxy_pass to gunicorn.

Volume:

* ./wowa/static_root -> /data/static
* ./wowa/media -> /data/media
* ./.nginx/log -> /var/log/nginx
* ./.nginx/sites-enabled -> /etc/nginx/sites-enabled

LICENSE
=============
This software is distributed using MIT license, see LICENSE file for more details.
