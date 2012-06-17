#!/usr/bin/python3
from quick2wire.gpio import Pin
import time

o1 = Pin(11, Pin.Out)
o2 = Pin(13, Pin.Out)
o3 = Pin(15, Pin.Out)
o4 = Pin(16, Pin.Out)
while True:
    for p in o1,o2,o3,o4,o3,o2:
        p.value=1
        time.sleep(0.05)
        p.value=0


