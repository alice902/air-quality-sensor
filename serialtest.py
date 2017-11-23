import serial

port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)

while True:
	rcv = port.read(32)
	print('{} \n'.format(rcv))
