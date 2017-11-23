#!/usr/bin/env python3

import serial

port = serial.Serial("/dev/serial0", baudrate=9600, parity=PARITY_NONE, bytesize=EIGHTBITS, stopbits=STOPBITS_ONE)

while True:
	data = port.read()
	if data:
		dupa = data.encode('hex')
	print('{}'.format(dupa))
