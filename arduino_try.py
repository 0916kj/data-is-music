# -*- coding: utf-8 -*-
"""
Set up script to interface Arduino with computer

Tutorial: https://www.makeuseof.com/tag/program-control-arduino-python/

Use pyfirmata module: https://github.com/tino/pyFirmata
"""

from pyfirmata import Arduino, util
import time

##Check which COM port you are using in the Arduino IDE, and enter it into your code as the variable board.
board = Arduino('COM3')

##Now you’ll set up the user prompt. Those familiar with Python will recognize everything here.
##You print a question to the screen using the input function, and store the answer as a variable.
##Once the user has provided a number, the program reports back how many times the LED will blink.
loopTimes = raw_input('How many times would you like the LED to blink: ')
print('Blinking ' + loopTimes + ' times.')
