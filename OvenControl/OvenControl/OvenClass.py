import serial

class OvenClass(object):
    """This class implements the shared parameters for controlling our two oven heaters."""

    def __init__(self, comPort, iD):
        self.iD=iD
        self.comPort = comPort
        self.error=False
        self.setpoint=-1
        self.temperature=-1
        self.ser = -1
        self.connectionStatus=False

    def read_setpoint(self):
        self.error=False

    def write_setpoint(self,setpoint):
        self.error=False

    def read_temperature(self):
        self.error=False
    
    def read_iD(self):
        self.error=False

    def open_connection(self):
        self.ser = serial.Serial(
            port=self.comPort,
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS
        )
        self.connectionStatus = self.ser.isOpen()



    def close_connection(self):
        self.ser.close()





      





