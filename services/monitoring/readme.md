#
## start up

### install
sudo apt update

sudo apt install git
sudo apt install python3.8-venv

1. create directory **usr/local/monitor**
2. copy from **./monitoring** to **usr/local/monitor/**
3. create virtual enviroment: **python3 -m venv .venv**
4. activate venv: **source .venv/bin/activate**
5. install dependences: **pip install -r requirments**

### create systemd service

sudo nano /etc/systemd/system/monitor.service

past there content below:

[Unit]
Description=Metricsmonitoring client
After=network.target

[Service]
WorkingDirectory=/usr/local/monitor
ExecStart=/usr/local/monitor/agent.py premix server 10 >/dev/null 2>&1 &
Restart=on-abort
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target

### enable and start service

sudo systemctl enable monitor

sudo systemctl start monitor
