#!/usr/bin/env python3

import serial																			# import modules
import requests
import time

pmsensor = serial.Serial('/dev/serial0')												# serial port configuration
pmsensor.baudrate = 9600																# and transmission parameters
pmsensor.bytesize = serial.EIGHTBITS
pmsensor.parity = serial.PARITY_NONE
pmsensor.stopbits = serial.STOPBITS_ONE

USER = 'root'																			# database credentials: username	
PASS = 'root'																			# password
URL_STRING = 'http://localhost:8086/write?db=raspi_measurements'						# and database url
SLEEP_TIME = 60																			# delay time between each measurement
FAN_WARMUP_TIME = 30

def main():
	time.sleep(FAN_WARMUP_TIME)
	try:
		while True:																		# infinite loop
			data_frame = bytearray(32)													# frame initialisation
			pmsensor.readinto(data_frame)												# writing readings from sensor to data_frame
			data = [int.from_bytes(data_frame[2*i:2*i+2], 'big') for i in range(16)]	# conversion from bytearray to 16-bit data list
			raw_data = "particulate_matter pm_1={},pm_25={},pm_10={}"					# raw string (request pattern)
			data_string = raw_data.format(data[2], data[3], data[4])					# formatted string
			r = requests.post(URL_STRING, auth=(USER,PASS), data=data_string)			# database request (returns code 204)
			time.sleep(SLEEP_TIME)														# delay
	except KeyboardInterrupt:															# keyboard interrupt exception
		pass

if __name__ == "__main__":																# main function (run as a script)
	main()
