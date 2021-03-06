#!/usr/bin/env bash
# Task 0 of deploiment
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World" |sudo tee  /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu  -hR /data/
sudo sed -i '47i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
