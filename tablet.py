# File created 26/01/2015
# Contains main method to write Braille output to a tablet

# Pins are [12, 16, 18, 22, 24, 26] in GPIO.BOARD mode

import RPi.GPIO as GPIO
import time
import atexit
from braille_dict import braille_dict

led_pins = [12, 16, 18, 22, 24, 26]

def main():
	# Set up GPIO
	GPIO.setmode(GPIO.BOARD)
	for pin in led_pins:
		GPIO.setup(pin, GPIO.OUT)
	atexit.register(cleanup)
	print "Enter sentences for Braille display"
	while True:
		display_str = raw_input('-> ')
		for c in display_str:
			display_character(c)
			time.sleep(0.9)
			display_character(' ')
			time.sleep(0.1)
		# Clear single character display
		display_character(' ')

def cleanup():
	print "Cleaning up..."
	GPIO.cleanup()

def display_string(s):
	""" Given a string,sc, displays the Braille equivalent on
	the LEDs with the global pin values. """
	assert type(s) == str
	# Buffer for complete conversion of string
	buf = []
	for c in s:
		buf += char_to_braille(c)
	for pin, val in zip(led_pins, buf):
		GPIO.output(pin, val)

def char_to_braille(c):
	""" Given a character, c, returns a list of six bool values
	for display on the LEDs """
	assert type(c) == str and len(c) == 1
	if braille_dict.has_key(c):
		return braille_dict[c]
	else:
		return [[False]*6]

if __name__ == '__main__':
	main()

