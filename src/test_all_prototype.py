import RPi.GPIO as GPIO
import time
import atexit

row_pins = [8, 10, 12, 16, 18, 22, 24, 26, 23]
col_pins = [21, 19, 15, 13]

def cleanup():
    GPIO.cleanup()
    print "Finished. Cleaning up..."

GPIO.setmode(GPIO.BOARD)

for col_pin in col_pins:
    GPIO.setup(col_pin, GPIO.OUT)
    GPIO.output(col_pin, GPIO.LOW)

for row_pin in row_pins:
    GPIO.setup(row_pin, GPIO.OUT)
    GPIO.output(row_pin, GPIO.HIGH)

atexit.register(cleanup)

print "Outputting all cells consecutively for 0.3s each"

for col_pin in col_pins:
    GPIO.output(col_pin, GPIO.HIGH)
    print str(col_pin) + ": "
    for row_pin in row_pins:
        GPIO.output(row_pin, GPIO.LOW)
        print row_pin
        time.sleep(.3)
        GPIO.output(row_pin, GPIO.HIGH)
    print " "
    GPIO.output(col_pin, GPIO.LOW)

cleanup()
