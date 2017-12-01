#!/usr/bin/env python3

import Adafruit_DHT																	# import modules
import requests
import time

USER = 'root'																		# database credentials: username	
PASS = 'root'																		# password
URL_STRING = 'http://localhost:8086/write?db=raspi_measurements'					# and database url
SLEEP_TIME = 60																		# delay time between each measurement

def main():
	try:
		while True:																	# infinite loop
			humidity, temperature = Adafruit_DHT.read_retry(22, 4)					# dht22 sensor readings
			raw_data = "temp_and_hum temperature={},humidity={}"					# raw string (request pattern)
			data_string = raw_data.format(round(temperature,1),round(humidity,1)) 	# formatted string
			r = requests.post(URL_STRING, auth=(USER,PASS), data=data_string)		# database request (returns code 204)
			time.sleep(SLEEP_TIME)													# delay
	except KeyboardInterrupt:														# keyboard interrupt exception
		pass
		
if __name__ == "__main__":
	main()																			# main function
