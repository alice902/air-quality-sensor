#!/usr/bin/env python

import serial


pmsensor = serial.Serial('/dev/serial0')
pmsensor.baudrate = 9600
pmsensor.bytesize = serial.EIGHTBITS
pmsensor.parity = serial.PARITY_NONE
pmsensor.stopbits = serial.STOPBITS_ONE
print(pmsensor.name)					# chceck which port was really used

while True:
	frame_buffer = bytearray(buffer,32)
	pmsensor.readinto(frame_buffer)	
	dupa=str(frame_buffer,hex)
	print(dupa)
#serial.threaded.ReaderThread.connect()
#serial.threaded.ReaderThread.run()


#pmsensor.close()					# close port
