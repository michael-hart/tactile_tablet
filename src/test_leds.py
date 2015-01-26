import time
import RPi.GPIO as GPIO

pins = [ 12, 16, 18, 22, 24, 26 ]
GPIO.setmode(GPIO.BOARD)

for pin in pins:
	GPIO.setup( pin, GPIO.OUT )

for pin in pins:
	GPIO.output(pin, True)
	time.sleep(0.2)
	GPIO.output(pin, False)

GPIO.cleanup()
