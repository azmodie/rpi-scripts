#!/usr/bin/python3

import time
from quick2wire.gpio import Pin

# import pins for output
out_pin1 = Pin(11, Pin.Out)
out_pin2 = Pin(13, Pin.Out)
out_pin3 = Pin(15, Pin.Out)
out_pin4 = Pin(16, Pin.Out)

# import pins for input 
in_pin = Pin(7, Pin.In)

# init count
count = 0

print ("This script will increase a counter every time the button is pressed")
print ("Please press the button")

# outputs binary reprisentation to 4 leds that matches count. 
def display_count(i):
    out_pin4.value = bin(i)[-1] if len(bin(i))>2 else 0
    out_pin3.value = bin(i)[-2] if len(bin(i))>3 else 0
    out_pin2.value = bin(i)[-3] if len(bin(i))>4 else 0
    out_pin1.value = bin(i)[-4] if len(bin(i))>5 else 0
	print ("binary output " + out_pin1.value + output_pin2.value + out_pin3.value + out_pin4.value)

try:
	while True:
		mybutton = in_pin.value # get input value of button
		if mybutton == False:
			count = count + 1
			display_count(count)
			print ("counter is  " + count") 
			time.sleep(.2)
		if count == 16: # reset counter at 16
			print ("counter reset") 
			count = 0

except KeyboardInterrupt: # trap ctrl+c to cleanly unexport pins
        out_pin.unexport()
        in_pin.unexport()
