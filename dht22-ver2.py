#!/usr/bin/env python3

import Adafruit_DHT
import requests
import time

USER = 'root'
PASS = 'root'
url_string = 'http://localhost:8086/write?db=raspi_measurements'

while True:
	humidity, temperature = Adafruit_DHT.read_retry(22, 4)
	raw_data = "temp_and_hum temperature={},humidity={}"
	data_string = raw_data.format(round(temperature,1),round(humidity,1)) 
	r = requests.post(url_string, auth=(USER,PASS), data=data_string)
	time.sleep(10)
