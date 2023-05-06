import sys

import RPi.GPIO as GPIO

import dht11

import time

import datetime

import requests



myAPI = 'PL0FQK5P82YX909X' 

ThingsURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 



# initialize GPIO

GPIO.setwarnings(True)

GPIO.setmode(GPIO.BCM)



# read data using pin 14

instance = dht11.DHT11(pin=4)

try:

    while True:

        result = instance.read()

        if result.is_valid():

            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)

            print("Humidity: %-3.1f %%" % result.humidity)

            r = requests.post(ThingsURL + '&field1=%s&field2=%s' % (result.temperature, result.humidity))

            print(r.text)

        time.sleep(6)



except KeyboardInterrupt:

    print("Cleanup")

    GPIO.cleanup()



			

	