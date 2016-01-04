#Manual oven temperature control file. Use this to tell the oven to change the reservoir setpoint!

import serial
import sys #call sys.exit() to exit program, useful for errors
from OvenClass import OvenClass

#Useful variables
newNozzleSetpoint = -1 #Not currently implemented
newReservoirSetpoint = -1
string = 'none'
error = False
errorMessage = 'None'

#Assign com ports and iD's
nozzleCOM='COM2'
reservoirCOM='COM5'
nozzleID=1
reservoirID=2

#Assign an oven object to nozzle and reservoir
nozzle=OvenClass(nozzleCOM) 
reservoir=OvenClass(reservoirCOM)

#Read current setpoints and temperatures, then display
nozzle.read_setpoint()
nozzle.read_temperature()
reservoir.read_setpoint()
reservoir.read_temperature()

#First step is always to check that the com ports are right
if nozzle.iD != nozzleID or reservoir.iD != reservoirID:
    print('COM Ports do not match controllers... BAD!')
    raw_input("Press enter to continue...")
    sys.exit()




#Print current values
print('Nozzle setpoint: '+ str(nozzle.setpoint))
print('Nozzle temperature: ' + str(nozzle.temperature))
print('Reservoir setpoint: ' + str(reservoir.setpoint))
print('Reservoir temperature: ' + str(reservoir.temperature))

#Get new setpoint - only reservoir temp for now since we never change the nozzle convert to int
newReservoirSetpoint = float(input('Please enter a new reservoir setpoint in integer format: '))


#Error checking - make sure that the input temp isn't too crazy. 
#Case: Is the new setpoint within 25 degrees of the temp and previous setpoint?
if abs(newReservoirSetpoint-reservoir.setpoint) > 25.0 or abs(newReservoirSetpoint-reservoir.temperature) > 25.0:
    error = True
    errorMessage = 'New reservoir setpoint is >25 degrees from previous setpoint/temperature.'



#Exit the program without changing if there is an error.
if error == True:
    print('ERROR:')
    print(errorMessage)
    print('The setpoint has not been changed.')
else:
    #Valid input, so new setpoint!
    reservoir.write_setpoint(newReservoirSetpoint)
    print('No error, setpoint is changed!')
    
    #Read current setpoints and temperatures, then display
    nozzle.read_setpoint()
    nozzle.read_temperature()
    reservoir.read_setpoint()
    reservoir.read_temperature()

    #Print current values
    print('Nozzle setpoint: '+ str(nozzle.setpoint))
    print('Nozzle temperature: ' + str(nozzle.temperature))
    print('Reservoir setpoint: ' + str(reservoir.setpoint))
    print('Reservoir temperature: ' + str(reservoir.temperature))


#raw_input("Press enter to continue...")


