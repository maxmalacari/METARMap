/usr/bin/sudo pkill -F /home/pi/offpid.pid
/usr/bin/sudo pkill -F /home/pi/metarpid.pid
/usr/bin/sudo pkill -F /home/pi/metarlcdpid.pid
/usr/bin/sudo pkill -F /home/pi/offlcdpid.pid
/usr/bin/sudo /usr/bin/python3 /home/pi/metar/METARMap/pixelsoff.py & echo $! > /home/pi/offpid.pid
/usr/bin/sudo /usr/bin/python3 /home/pi/metar/METARMap/stopLCD.py & echo $! > /home/pi/offlcdpid.pid
