#!/bin/sh
# camera.sh
# will run the move.py and send.py scripts with processing

cd /
cd /home/pi
sudo python move.py
sudo python detect_plants.py
sudo python send.py
echo "Done!"