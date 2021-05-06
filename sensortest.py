import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.AM2302
DHT_PIN = 4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(temperature)
    else:
        print("Failed to retrieve data from humidity sensor")
