#!/usr/bin/python3

import time
from quick2wire.gpio import Pin

out_pin = Pin(11, Pin.Out)
out_pin.value = 0
print ("pin 11 value = ", out_pin.value)

try:
	while True:
		out_pin.value = 1 - out_pin.value
		print ("pin 11 value = ", out_pin.value)
		time.sleep(2)

except KeyboardInterrupt:
        out_pin.unexport()

