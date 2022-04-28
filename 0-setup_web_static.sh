#!/usr/bin/env bash
# Task 0 of deploiment
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown ubuntu:ubuntu  -hR /data/
sed -i '47i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx start
