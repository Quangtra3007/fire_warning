import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def GPIO_on(gpionumber):
	if(GPIO.gpio_function(gpionumber) != GPIO.OUT):
		GPIO.setup(gpionumber, GPIO.OUT)
	GPIO.output(gpionumber, GPIO.HIGH)
	
def GPIO_off(gpionumber):
	GPIO.output(gpionumber, GPIO.LOW)
	
