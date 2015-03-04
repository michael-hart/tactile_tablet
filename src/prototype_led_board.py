'''
Created on 9 Feb 2015

@author: Michael
'''

from braille_dict import braille_dict as bdict
import RPi.GPIO as GPIO
import atexit
import itertools

# Set value for each row
row_pins = [8, 10, 12, 16, 18, 22, 24, 26, 23]
# Select column
column_pins = [21, 19, 15, 13]

def main():
    """ Main function to generate pure braille characters in a 2x3 formation with set pins and display them
        on the single prototype LED board. This file has a specific use. """
    # Set up GPIO, off by default
    GPIO.setmode(GPIO.BOARD)
    for pin in row_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    for pin in column_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    atexit.register(cleanup)
    
    buf = [ 
       [bdict['a'][0], bdict['b'][0]],
       [bdict['c'][0], bdict['d'][0]], 
       [bdict['e'][0], bdict['f'][0]] ]
    
    column_dict = {}
    for col, col_pin in enumerate(column_pins):
        values = []
        for r in buf:
            if col%2 == 0:
                values += r[col/2][0:3]
            else:
                values += r[col/2][5:2:-1]
    
        column_dict[col_pin] = list(values)
        
    # Printed sanity check on numbers. See logbook for expected result
    for key, val in column_dict.items():
        print str(key) + ": " + str([str(x)[0] for x in val])
        
    while True:
        for col_pin in column_pins:
            GPIO.output(col_pin, GPIO.HIGH)
            for row_pin, val in itertools.izip(row_pins, column_dict[col_pin]):
                GPIO.output(row_pin, val)
            GPIO.output(col_pin, GPIO.LOW)
	    for row_pin in row_pins:
		GPIO.output(row_pin, GPIO.HIGH)
        
def cleanup():
    print "Cleaning up..."
    GPIO.cleanup()
        

if __name__ == '__main__':
    main()
