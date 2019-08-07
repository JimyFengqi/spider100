#!/usr/bin/python3.6 

import os,random
imagedir=os.path.expandvars('$HOME')+"/Pictures/Bing/"
print(imagedir)
imagefile=imagedir+random.choice(os.listdir(imagedir))
cmd='gsettings set org.gnome.desktop.background picture-uri file:'+imagefile
print(cmd)
os.system(cmd)
