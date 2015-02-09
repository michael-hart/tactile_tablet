# File created 26/01/2015
# Contains main method to write Braille output to a tablet

# Pins are [12, 16, 18, 22, 24, 26] in GPIO.BOARD mode

import RPi.GPIO as GPIO
import time
import atexit
from braille_converter import convert_string

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
		char_buffer = convert_string(display_str)
		for c in char_buffer:
			for pin, val in zip(led_pins, c):
				GPIO.output(pin, val)
			time.sleep(0.5)

def cleanup():
	print "Cleaning up..."
	GPIO.cleanup()

if __name__ == '__main__':
	main()
