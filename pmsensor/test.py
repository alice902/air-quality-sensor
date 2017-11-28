#!/usr/bin/python3

frame=bytearray.fromhex('42 4d 00 1c 00 29 00 3e 00 46 00 1f 00 2e 00 3c 19 ec 07 bf 01 69 00 36 00 08 00 00 91 00 04 e5')

print(frame)
print(frame.hex())

print(len(frame))

if len(frame) != 32
	print('Bad frame')
