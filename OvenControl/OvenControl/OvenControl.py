import serial
from OvenClass import OvenClass

nozzleCOM='COM2'
resCOM='COM5'

nozzle=OvenClass(nozzleCOM,1)
reservoir=OvenClass(resCOM,2)

nozzle.open_connection
nozzle.close_connection

print(nozzle.error)

print('Hello World!')