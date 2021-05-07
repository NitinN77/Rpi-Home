import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
print "LED on"
GPIO.output(20,GPIO.HIGH)
time.sleep(5)
print "LED off"
GPIO.output(20,GPIO.LOW)

DHT_SENSOR = Adafruit_DHT.AM2302
DHT_PIN = 4
#while True:
#    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
#    if humidity is not None and temperature is not None:
#        print(temperature)
#    else:
#        print("Failed to retrieve data from humidity sensor")


