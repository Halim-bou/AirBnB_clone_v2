#!/usr/bin/env bash
#Script that setup my web servers for the seployment of web static
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<h1>Hello there<h1>">/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
old="server_name _;"
new="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t}"
sudo sed -i "s|$old|$new|" /etc/nginx/sites-available/default
sudo service nginx restart
