#Program for heating up the oven to 575 for the nozzle and 375 for the reservoir

#Import statements
import serial
import time
import sys #call sys.exit() to exit program, useful for errors
from OvenClass import OvenClass

#Useful variables
newNozzleSetpoint = -1.0 
newReservoirSetpoint = -1.0
maxNozzleTemperature = 575.0
maxReservoirTemperature = 375.0
totalTime = 0
timeInterval=300 #seconds

#Assign com ports and iD's which are checked 
nozzleCOM='COM2'
reservoirCOM='COM5'
nozzleID=1
reservoirID=2

#Assign an oven object to nozzle and reservoir
nozzle=OvenClass(nozzleCOM) 
reservoir=OvenClass(reservoirCOM)

#Read current setpoints, temps, and iD numbers. Set reservoir newsetpoint for later reference
nozzle.read_setpoint()
nozzle.read_temperature()
nozzle.read_iD()
reservoir.read_setpoint()
reservoir.read_temperature()
reservoir.read_iD()
newReservoirSetpoint=reservoir.setpoint

#First step is always to check that the com ports are right so that the nozzle and reservoir aren't mixed!
if nozzle.iD != nozzleID or reservoir.iD != reservoirID:
    print('COM Ports do not match controllers... BAD!')
    raw_input("Press enter to continue...")
    sys.exit()


#
#To add: section for bad start temps
#

#Step one: Set nozzle setpoint to 400 to start off. End code if it didn't write
newNozzleSetpoint=400.0
nozzle.write_setpoint(newNozzleSetpoint)
nozzle.read_setpoint()
#Catch if first nozzle setpoint write didn't happen
if nozzle.setpoint != newNozzleSetpoint:
    print('Nozzle to 400 didnt write! Error!')
    raw_input("Press enter to continue...")
    sys.exit()
    
#Step two - main nozzle loop.
while newNozzleSetpoint < maxNozzleTemperature:
    nozzle.read_temperature()
    reservoir.read_temperature()
    
    #Nozzle handling case. If temp is high enough add 25 degrees to it!
    if nozzle.temperature > newNozzleSetpoint -5.0:
        newNozzleSetpoint=newNozzleSetpoint+25.0
        nozzle.write_setpoint(newNozzleSetpoint)
        nozzle.read_setpoint()
        

    #Reservoir handling case
    if reservoir.temperature > reservoir.setpoint:
        newReservoirSetpoint = reservoir.temperature
        reservoir.write_setpoint(newReservoirSetpoint)
        reservoir.read_setpoint()
        
    #Check for setpoints matching and being written
    if nozzle.setpoint != newNozzleSetpoint or reservoir.setpoint != newReservoirSetpoint:
        print('Nozzle loop reservoir or nozzle setpoint didnt write. Error!')
        raw_input("Press enter to continue...")
        sys.exit()

    #As a safety check kill the program if the loop has a setpoint over 575 or 375 for the noz and res
    if nozzle.setpoint > 575.0 or reservoir.setpoint > 375.0:
        print('MAJOR ISSUE SETPOINTS ARE TOO HIGH')
        reservoir.write_setpoint(min(375.0,reservoir.temperature))
        nozzle.write_setpoint(min(575.0,nozzle.temperature))
        raw_input("Press enter to continue...")
        sys.exit()
 
    #Print current values, update time, sleep
    print('Total time in minutes: ' + str(totalTime/60))
    print('Nozzle setpoint: '+ str(nozzle.setpoint))
    print('Nozzle temperature: ' + str(nozzle.temperature))
    print('Reservoir setpoint: ' + str(reservoir.setpoint))
    print('Reservoir temperature: ' + str(reservoir.temperature))
    totalTime=totalTime+300 #add 5 minutes to time
    time.sleep(timeInterval)
    
#Step three - main reservoir loop. Take reservoir to 15 less than max, 5 degree steps
while newReservoirSetpoint < maxReservoirTemperature-15.0:
    nozzle.read_temperature()
    reservoir.read_temperature()        

    #Reservoir handling case
    if reservoir.temperature > reservoir.setpoint:
        newReservoirSetpoint = newReservoirSetpoint+5
        reservoir.write_setpoint(newReservoirSetpoint)
        reservoir.read_setpoint()
        
    #Check for setpoint matching and being written
    if reservoir.setpoint != newReservoirSetpoint:
        print('Reservoir loop reservoir setpoint didnt write. Error!')
        raw_input("Press enter to continue...")
        sys.exit()

    #As a safety check kill the program if the loop has a setpoint over 575 or 375 for the noz and res
    if nozzle.setpoint > 575.0 or reservoir.setpoint > 375.0:
        print('MAJOR ISSUE SETPOINTS ARE TOO HIGH')
        reservoir.write_setpoint(min(375.0,reservoir.temperature))
        nozzle.write_setpoint(min(575.0,nozzle.temperature))
        raw_input("Press enter to continue...")
        sys.exit()
 
    #Print current values, update time, sleep
    print('Total time in minutes: ' + str(totalTime/60))
    print('Nozzle setpoint: '+ str(nozzle.setpoint))
    print('Nozzle temperature: ' + str(nozzle.temperature))
    print('Reservoir setpoint: ' + str(reservoir.setpoint))
    print('Reservoir temperature: ' + str(reservoir.temperature))
    totalTime=totalTime+300 #add 5 minutes to time
    time.sleep(timeInterval)
        

#Step four wait for reservoir overshoot and catch it for the final reservoir set. First wait timeinterval, then read temp
time.sleep(timeInterval) 
totalTime=totalTime+300 #add 5 minutes to time
nozzle.read_temperature()
reservoir.read_temperature()
#Now excute while loop which waits
while reservoir.temperature > reservoir.setpoint:
    reservoir.read_temperature()
    newReservoirSetpoint=reservoir.temperature #set new setpoint to temp
    print('Temp for reservoir still rising')
    time.sleep(timeInterval)
    totalTime=totalTime+300 #add 5 minutes to time

#Now set the reservoir setpoint to the min of the newsetpoint.
reservoir.write_setpoint(min(newReservoirSetpoint,375.0))
nozzle.read_setpoint()
nozzle.read_temperature()
reservoir.read_setpoint()
reservoir.read_temperature()

#Print all the data one more time
print('Nozzle setpoint: '+ str(nozzle.setpoint))
print('Nozzle temperature: ' + str(nozzle.temperature))
print('Reservoir setpoint: ' + str(reservoir.setpoint))
print('Reservoir temperature: ' + str(reservoir.temperature))
print('Time to complete in minutes: ' + totalTime)





