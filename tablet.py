# File created 26/01/2015
# Contains main method to write Braille output to a tablet

# Pins are [12, 16, 18, 22, 24, 26] in GPIO.BOARD mode

import RPi.GPIO as GPIO
import time
import atexit

led_pins = [12, 16, 18, 22, 24, 26]

def main():
	# Set up GPIO
	GPIO.setmode(GPIO.BOARD)
	for pin in led_pins:
		GPIO.setup(pin, GPIO.OUT)
	atexit.register(cleanup)
	while True:
		pass

def cleanup():
	print "Cleaning up..."
	GPIO.cleanup()

def display_character(c):
	""" Given a character, c, displays the Braille equivalent on
	the LEDs with the global pin values. """
	pass

def char_to_braille(c):
	""" Given a character, c, returns a list of six bool values
	for display on the LEDs """
	pass

if __name__ == '__main__':
	main()

