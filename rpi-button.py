#!/usr/bin/python3

import time
from quick2wire.gpio import Pin

out_pin = Pin(11, Pin.Out)
in_pin = Pin(7, Pin.In)

try:
	while True:
		mybutton = in_pin.value
		out_pin.value = 0
		if mybutton == False:
			print ("giggle")
			out_pin.value = 1 - out_pin.value
			time.sleep(.2)
			
except KeyboardInterrupt:
	out_pin.unexport()
	in_pin.unexport()


