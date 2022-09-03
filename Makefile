

install_directory=/usr/local/

.DELETE_ON_ERROR:
all: create install
create:
	cp services/*.services /etc/systemd/system
	mkdir -p ${/usr/local/vnc_server} && cp services/vnc_server/x0vncserver.sh /usr/local/vnc_server

install: create
	/bin/bash ./services/monitoring/install.sh
