import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0
lastVal = True
while(True):
	inputVal = GPIO.input(12)
	if(lastVal != inputVal):
		lastVal = inputVal
		if(inputVal):
			count += 1
			print count
	time.sleep(0.01)

