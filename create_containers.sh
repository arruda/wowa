#!/bin/bash
sudo docker run -d -p 5432:5432 --name wowadb wowadb
sudo docker run -t -i -d -p 8001:8000 --link wowadb:db -v $(pwd):/home/docker/proj --name wowaapp wowaapp
sudo docker run -t -i -d -p 8000:80 --link wowaapp:app -v $(pwd)/.nginx/sites-enabled:/etc/nginx/sites-enabled -v $(pwd)/.nginx/log:/var/log/nginx -v $(pwd)/wowa/static_root:/data/static -v $(pwd)/wowa/media:/data/media --name wowanginx wowanginx