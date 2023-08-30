#!/bin/bash
sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

sudo cp ./app.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl start app

sudo systemctl enable app

sudo apt install nginx -y
# Server block
sudo cp ./app /etc/nginx/sites-available/app

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled

sudo nginx -t

sudo chmod 775 -R /home/ubuntu/test
sudo chmod 775 -R /home/ubuntu

sudo systemctl restart nginx

printf "App Is Live\n"
