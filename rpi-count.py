#!/usr/bin/python3

import time
from quick2wire.gpio import Pin

out_pin1 = Pin(11, Pin.Out)
out_pin2 = Pin(13, Pin.Out)
out_pin3 = Pin(15, Pin.Out)
out_pin4 = Pin(16, Pin.Out)

in_pin = Pin(7, Pin.In)

try:
        while True:
                mybutton = in_pin.value
                if mybutton == False:
					count = count + 1
					display_count(count)
					time.sleep(.2)
                        
except KeyboardInterrupt:
        out_pin.unexport()
        in_pin.unexport()

def display_count(i):
        out_pin4.value = bin(i)[-1] if len(bin(i))>2 else 0
        out_pin3.value = bin(i)[-2] if len(bin(i))>3 else 0
        out_pin2.value = bin(i)[-3] if len(bin(i))>4 else 0
        out_pin1.value = bin(i)[-4] if len(bin(i))>5 else 0

