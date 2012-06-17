#!/usr/bin/python3
import dectobin #Module...defined later
import string #Module.....defined later

a=int(raw_input("Enter a decimal number: "))

if a<0:
	print ("Try entering a positive number/0 ")
elif a==0:
	print ("Binary: 0")
else:
	list=dectobin.conv(a)
	list1=string.format(list)

print ("Binary: " ,list1)
