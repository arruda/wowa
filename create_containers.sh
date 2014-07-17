#!/bin/bash
sudo docker run -P -d --name wowadb wowadb

sudo docker run -d -p 8000:80 --link wowadb:db -v $(pwd):/home/docker/proj --name wowaapp wowa