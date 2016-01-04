#This file is for testing purposes and will not be for the heating, cooling, or manual controls.

import serial
import time
from OvenClass import OvenClass

#COM port definitions for nozzle and reservoir
nozzleCOM='COM2'
resCOM='COM5'

#Assign a oven class object for each reservoir and nozzle
nozzle=OvenClass(nozzleCOM,1)
reservoir=OvenClass(resCOM,2)



nozzle.open_connection()
nozzle.close_connection()

print(nozzle.error)

temp=hex(1000)
temp=temp[2:]
print(temp)

print('Hello World!')