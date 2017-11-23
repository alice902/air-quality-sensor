#!/usr/bin/env python3

import serial


pmsensor = serial.Serial('/dev/serial0')
pmsensor.baudrate = 9600
pmsensor.bytesize = serial.EIGHTBITS
pmsensor.parity = serial.PARITY_NONE
pmsensor.stopbits = serial.STOPBITS_ONE
	

print(pmsensor.name)					# chceck which port was really used
pmsensor.close()					# close port
