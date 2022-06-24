#! /bin/bash
echo "Undate apts"
sudo apt-get update
echo "Install python3"
sudo apt-get install python3
echo "Install pip3"
sudo apt-get -y install python3-pip
echo "Setup virtual environment"
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
