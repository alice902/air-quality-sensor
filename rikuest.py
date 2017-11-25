import requests
import time

user = 'root'
password = 'root'

while True:
	url_string = 'http://localhost:8086/write?db=dupa'
	raw_data = "temp_and_hum,temperature={} humidity={}"
	temp = 29
	hum = 66
	data_string = raw_data.format(temp,hum) 
	print(data_string)
	r = requests.post(url_string, auth=(user, password), data=data_string)
	time.sleep(3)


