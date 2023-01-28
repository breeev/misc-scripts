#!/usr/bin/python3

from os import system
from subprocess import Popen, PIPE
from re import findall

for i in findall(r'\\tid=(\d+)', str(Popen('xinput list | grep -i mouse', stdout=PIPE, shell=True).communicate()[0])): system('xinput set-prop '+i+' "libinput Scroll Method Enabled" 0, 0, 1')
