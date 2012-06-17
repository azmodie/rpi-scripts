#!/usr/bin/python3

from time import sleep
from quick2wire.gpio import Pin

pin = Pin(11, Pin.Out)

try:
    while True:
        pin.value = 1 - pin.value
        sleep(1)
except KeyboardInterrupt:
    pin.unexport()
