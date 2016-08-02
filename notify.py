#!/usr/bin/env python

# 
# https://software.intel.com/en-us/blogs/2015/05/05/efficient-data-sharing-using-interrupts-on-intel-edison
# 

import mraa
import time
import json
import sys

#class Counter:
#  count = 0

#c = Counter()

# inside a python interrupt you cannot use 'basic' types so you'll need to use
# objects
#def test(gpio):
#  print("pin " + repr(gpio.getPin(True)) + " = " + repr(gpio.read()))
#  c.count+=1

def subscriberEvent(gpio):
	if repr(gpio.read()):
		with open("climdata.txt", "r") as f:
			contents = f.read()
			print ("Message from Arduino: " + contents)

pin = 1;

if (len(sys.argv) == 2):
  try:
    pin = int(sys.argv[1], 10)
  except ValueError:
    printf("Invalid pin " + sys.argv[1])
try:
    x = mraa.Gpio(pin)
    print("Starting ISR for pin " + repr(pin))
    x.dir(mraa.DIR_IN)
    x.isr(mraa.EDGE_BOTH, subscriberEvent, x)
    var = raw_input("Press ENTER to stop")
    x.isrExit()
except ValueError as e:
    print(e)


