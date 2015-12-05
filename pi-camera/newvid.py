# This script uses raspivid to take a video converts it with MP4 box and plays it on a connected display
import os
os.system("mkdir /tmp/stream")
os.system("raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &")
os.system("omxplayer -p -o hdmi myvid.mp4")
