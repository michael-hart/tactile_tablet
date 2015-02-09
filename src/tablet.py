# File created 26/01/2015
# Contains main method to write Braille output to a tablet

# Pins are [12, 16, 18, 22, 24, 26] in GPIO.BOARD mode

import RPi.GPIO as GPIO
import time
import atexit
from braille_converter import convert_string
from braille_dict import braille_dict as bdict

led_pins = [12, 16, 18, 22, 24, 26]

def main():

	tablet_columns = 2
	tablet_rows = 3

	leftover_buffer = []

	# Set up GPIO
	GPIO.setmode(GPIO.BOARD)
	for pin in led_pins:
		GPIO.setup(pin, GPIO.OUT)
	atexit.register(cleanup)
	print "Enter sentences for Braille display"
	while True:
		display_str = raw_input('-> ')
		word_buffer = convert_string(display_str)
		word_buffer = leftover_buffer + word_buffer
		line_buffer, leftover_buffer = fit_to_screen(word_buffer, tablet_columns, tablet_rows, leftover_buffer)
		# TODO: Output line_buffer to display

def fit_to_screen(words, cols, rows):
	leftover = list(words)
	lines = []
	for i in range(rows):
		lines.append([])
		while len(lines[i]) + len(leftover[0]) + 1 < cols:
			lines[i] += leftover[0] + bdict[' ']
			leftover = leftover[1:]

	return lines, leftover


def cleanup():
	print "Cleaning up..."
	GPIO.cleanup()

if __name__ == '__main__':
	main()
