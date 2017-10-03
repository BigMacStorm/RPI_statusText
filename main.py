import RPi.GPIO as GPIO
import time

import Adafruit_CharLCD as LCD

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 21
lcd_d7 = 22
lcd_bl = 4

cols = 16
rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, cols, rows, lcd_bl)

lcd.message('Hello\nWorld!')


count = 0
lastVal = True
while(True):
	inputVal = GPIO.input(12)
	if(lastVal != inputVal):
		lastVal = inputVal
		if(inputVal):
			count += 1
			lcd.clear()
			lcd.message(str(count))
	time.sleep(0.01)

