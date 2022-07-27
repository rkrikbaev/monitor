#!/bin/bash
mkdir monitor
cd monitor

sudo apt-get update
sudo apt install python3.8-venv
python3 -m venv .venv
