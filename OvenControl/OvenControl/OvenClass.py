import serial

class OvenClass(object):
    """This class implements the shared parameters for controlling our two oven heaters."""

    #constructor
    def __init__(self, comPort):
        self.iD=-1
        self.comPort = comPort
        self.error=False
        self.setpoint=-1
        self.newSetpoint = -1
        self.temperature=-1
        self.ser = -1
        self.connectionStatus=False
        self.message = 'None!'
        self.read = 'None' #used to store read string of hex
        self.echo='None'

    #Read the setpoint from the controller and store it.
    def read_setpoint(self):
        self.open_connection()
        self.ser.write('*R01\r')
        self.read = self.ser.read(10)
        self.read=int(self.read[6:],16) #processing, get rid of leading characters that don't matter, convert to int from hex
        self.setpoint=float(self.read)/10 #convert the 4 digit int to a float and restore decimal place ie 2000 -> 200.0
        self.close_connection()

    #Write a new setpoint.
    def write_setpoint(self,newSetpoint):
        self.newSetpoint='*W01200'+hex(int(newSetpoint)*10)[2:].upper()+'\r' #hex gives lowercase, oven needs upper...
        self.open_connection()
        self.ser.write(self.newSetpoint)
        self.echo=self.ser.read(4)
        self.close_connection()
        
    
    #Reads the current temperature of the oven and stores it.
    def read_temperature(self):
        self.open_connection()
        self.ser.write('*X01\r')
        self.read = self.ser.read(9)
        self.temperature=float(self.read[3:])
        self.close_connection()

    #Reads the id of the oven controller - used to verify nozzle and reservoir are right!
    def read_iD(self):
        self.open_connection()
        self.ser.write('*R05\r')
        self.read = self.ser.read(7)
        self.iD=int(self.read[6:]) #convert to int so that it can be compared!
        self.close_connection()

    #Opens the connection to the oven and stores the object to the oven class - can be called by other functions in the oven class.
    def open_connection(self):
        self.ser = serial.Serial(
            port=self.comPort,
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS
        )

        #Set connection status to tell if it ran or not
        self.connectionStatus = self.ser.isOpen()
        

    #Close the oven connection!
    def close_connection(self):
        self.ser.close()
        self.connectionStatus = self.ser.isOpen()




      





