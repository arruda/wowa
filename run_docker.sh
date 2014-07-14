#!/bin/bash
sudo docker run -t -i -p 8000:80 -v $(pwd):/home/docker/proj  wowa