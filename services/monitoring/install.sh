#!/bin/bash
sudo apt-get update
sudo apt install python3.8-venv

mkdir monitor
cd monitor
python3 -m venv .venv

source .venv/bin/activate
pip install -r requirements.txt

