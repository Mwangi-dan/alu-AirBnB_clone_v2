#!/usr/bin/bash
# Script sets up my web servers for the deployment of web static
sudo apt-get -y  install nginx
sudo mkdir -p /data/web_static/releases/ /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "This is a test" | sudo touch /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /web_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
