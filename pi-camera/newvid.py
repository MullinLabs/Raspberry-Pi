# This script uses raspivid to take a video converts it with MP4 box and plays it on a connected display
import os
os.system("raspivid -o myvid.h264 -t 60000")
os.system("MP4Box -fps 30 -add myvid.h264 myvid.mp4")
os.system("rm myvid.h264")
os.system("omxplayer -p -o hdmi myvid.mp4")
