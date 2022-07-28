#! /bin/bash

DAEMON=/usr/bin/x0vncserver

test -x $DAEMON || exit 0

case "$1" in

start)
$DAEMON -passwordfile /home/user/.vnc/passwd -display :0>/dev/null 2>&1 &
;;

stop)
kill -9 $(ps -ef | grep /usr/bin/x0vncserver | grep -v grep | awk '{print $2}')
;;
*)
echo "Usage: $0 {start|stop|restart}"
exit 1
esac
exit 0