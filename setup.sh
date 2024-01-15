#!/bin/bash

echo "Gathering confetti...\n"

sudo apt-get update
sudo apt-get install -y python3 python3-pip nginx git tmux gunicorn certbot python3-certbot-nginx

echo "Cloning git repo...\n"

cd ~
git clone https://github.com/dustin-ctg/qrconfetti.git
cd qrconfetti

echo "Installing celebrations...\n"

pip3 install -r requirements.txt

echo "Making sure we can point the cannon to the right place.\n"
echo "Enter the domain that you would like to launch from: "

read domain_input

sudo certbot 

touch /etc/nginx/sites-available/qrconfetti
