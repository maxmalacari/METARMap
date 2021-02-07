/usr/bin/sudo pkill -F /home/pi/offpid.pid
/usr/bin/sudo pkill -F /home/pi/metarpid.pid
/usr/bin/sudo pkill -F /home/pi/metarlcdpid.pid
/usr/bin/sudo pkill -F /home/pi/offlcdpid.pid
/usr/bin/sudo /usr/bin/python3 /home/pi/metar/METARMap/metar.py & echo $! > /home/pi/metarpid.pid
/usr/bin/sudo /usr/bin/python3 /home/pi/metar/METARMap/metarLCD.py & echo $! > /home/pi/metarlcdpid.pid
