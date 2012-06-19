#!/usr/bin/python3

import time
import string
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

print ("This script will increase a counter")
print ("Every time the button is pressed")
print ("Display the counter and binary values")
print ("Please press the button")

# outputs binary reprisentation to 4 leds that matches count. 
def display_count(i):
	binvalue = bin(i)[2:].zfill(4)
	print ("Program output", binvalue)
	out_pin4.value = binvalue[-1]
	out_pin3.value = binvalue[-2]
	out_pin2.value = binvalue[-3]
	out_pin1.value = binvalue[-4]

try:
	while True:
		mybutton = in_pin.value # get input value of button
		if mybutton == False:
			count = count + 1
			if count == 16: # reset counter at 16
				print ("-= Counter Reset =-") 
				count = 0
			print ("Counter is  ", count)
			display_count(count)
			print ("Pin Output ")
			print ("Pin 1 2 3 4")  
			print ("   ", out_pin1.value,  out_pin2.value, out_pin3.value, out_pin4.value)
			time.sleep(.2)

except KeyboardInterrupt: # trap ctrl+c to cleanly unexport pins
		display_count(0)
		out_pin1.unexport()
		out_pin2.unexport()
		out_pin3.unexport()
		out_pin4.unexport()
		in_pin.unexport()
