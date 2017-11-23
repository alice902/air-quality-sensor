#!/usr/bin/env python3

import serial
import binascii


pmsensor = serial.Serial('/dev/serial0')
pmsensor.baudrate = 9600
pmsensor.bytesize = serial.EIGHTBITS
pmsensor.parity = serial.PARITY_NONE
pmsensor.stopbits = serial.STOPBITS_ONE
print(pmsensor.name)					# chceck which port was really used

while True:
	frame_buffer = bytearray(32)
	pmsensor.readinto(frame_buffer)
	dupa=binascii.hexlify(frame_buffer)
	print('{}'.format(dupa))
#serial.threaded.ReaderThread.connect()
#serial.threaded.ReaderThread.run()


#pmsensor.close()					# close port
