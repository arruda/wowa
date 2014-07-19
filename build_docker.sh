#!/bin/bash
sudo docker build -t wowanginx .nginx/
sudo docker build -t wowadb .pgserver/
sudo docker build -t wowa .