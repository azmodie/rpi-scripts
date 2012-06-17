#!/usr/bin/python3
from quick2wire.gpio import Pin
import time

o1 = Pin(11, Pin.Out)
o2 = Pin(13, Pin.Out)
o3 = Pin(15, Pin.Out)
o4 = Pin(16, Pin.Out)

for i in range(1,16):
    o4.value = bin(i)[-1] if len(bin(i))>2 else 0
    o3.value = bin(i)[-2] if len(bin(i))>3 else 0 
    o2.value = bin(i)[-3] if len(bin(i))>4 else 0
    o1.value = bin(i)[-4] if len(bin(i))>5 else 0
    time.sleep(0.5)


