#!/usr/bin/env python3

import serial

port = serial.Serial("/dev/serial0", 9600)

while True:
	data = port.read()
	if data:
		dupa = data.encode('hex')
	print('{}'.format(dupa))
