# 
# https://software.intel.com/en-us/blogs/2015/05/05/efficient-data-sharing-using-interrupts-on-intel-edison
# 

import mraa
import time
import json
import sys

def notifyWorld():
    notifier_pin.write(1)
    time.sleep(200)
    notifier_pin.write(0)

def subscriberEvent():

    with open("/arduino_notification_out.txt", "r") as f:
        contents = f.read()
        print "Message from Arduino: "
        print contents
    notifyWorld()

#/**********Read notification from arduino*************/
subscriber_pin = mraa.Gpio(1)
subscriber_pin.dir(mraa.DIR_IN)
subscriber_pin.isr(mraa.EDGE_RISING, subscriberEvent) 

notifier_pin = mraa.Gpio(5);
notifier_pin.dir(mraa.DIR_OUT);


