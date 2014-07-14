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
and then run `run_docker.sh` to run the container in the port 8000.

**obs**: The docker image uses supervisord, nginx and uwsgi to run the app.

LICENSE
=============
This software is distributed using MIT license, see LICENSE file for more details.
