#! /bin/bash
echo "Undate apts"
sudo apt-get update
echo "Install dependencies"
sudo apt-get -y install python3 python3-pip curl libreoffice unzip build-essential libssl-dev libffi-dev python3-dev python3-venv
echo "Setup virtual environment"
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
curl -o Fonts.zip -L https://github.com/InnoSWP/B21-07_DocToPDF/releases/latest/download/Fonts.zip
unzip Fonts.zip -d /root/.fonts/
rm Fonts.zip
