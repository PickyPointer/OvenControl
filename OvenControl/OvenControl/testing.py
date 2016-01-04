#Testing file for oven class and problems!

import serial
import sys #call sys.exit() to exit program, useful for errors
from OvenClass import OvenClass

#Assign com ports and iD's
nozzleCOM='COM2'
resCOM='COM5'
nozzleID=1
reservoirID=2

#Assign an oven object to nozzle and reservoir
nozzle=OvenClass(nozzleCOM)
reservoir=OvenClass(resCOM)

#Use the functions to test them
#nozzle.write_setpoint(200)
nozzle.read_temperature()
nozzle.read_setpoint()
nozzle.read_iD()
#reservoir.write_setpoint(100)
reservoir.read_temperature()
reservoir.read_setpoint()
reservoir.read_iD()


print('Nozzle temperature:')
print(nozzle.temperature)

print('Nozzle setpoint:')
print(nozzle.setpoint)

print('iD:')
print(nozzle.iD)


print('Reservoir temp:')
print(reservoir.temperature)

print('Reservoir setpoint:')
print(reservoir.setpoint)

print('Reservoir_iD:')
print(reservoir.iD)


