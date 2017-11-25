#!/usr/bin/env python3

import Adafruit_DHT
import time
import influxdb

from influxdb import InfluxDBClient

host = 'localhost'
port = '8086'
username = 'root'
password = 'root'
dbname = 'environment'
client = InfluxDBClient(host, port, username, password, dbname)

def get_data_points(temperature,timestamp):
	json_body = [
    	{
        	"measurement": "temperature_celcius",
       		 "tags": {
        	    "host": "raspi",
       		    "region": "kitchen"
       		 },
       	 	"time": timestamp,
       		"fields": {
       		     "value": temperature
       			 }
    }
]
	return json_body

while True:
	timestamp = time.ctime()
	humidity, temperature = Adafruit_DHT.read_retry(22, 4)
	print('{} temp: {:.1f}*C humidity: {:.1f}%'.format(timestamp, temperature, humidity))
	json_body = get_data_points(temperature,timestamp)
	client.write_points(json_body)
	time.sleep(10)
