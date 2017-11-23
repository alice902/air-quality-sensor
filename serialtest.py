#!/usr/bin/env python3

import serial

port = serial.Serial("/dev/serial0", serial.baudrate=9600, serial.parity=PARITY_NONE, serial.bytesize=EIGHTBITS, serial.stopbits=STOPBITS_ONE)

while True:
	data = port.read()
	if data:
		dupa = data.encode('hex')
	print('{}'.format(dupa))
