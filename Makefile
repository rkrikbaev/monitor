
vnc_server=/usr/local/vnc_server

create:
	cp services/*.services /etc/systemd/system
	mkdir -p ${/usr/local/vnc_server} && cp services/vnc_server/x0vncserver.sh /usr/local/vnc_server

install:
	/bin/bash ./services/monitoring/install.sh
