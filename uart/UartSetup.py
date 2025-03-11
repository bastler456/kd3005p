import serial


class UartSetup():
    def __init__(self, port: str,
                 baud: int = 9600,
                 bytesize: int = 8,
                 parity: str = 'N',
                 stopbits: int = 1,
                 timeout: int = 1,
                 xonxoff: int = 0,
                 rtscts: int = 0) -> None:
        self.__serial: serial = serial.Serial()
        self.__serial.port = port
        self.__serial.baudrate = baud
        self.__serial.bytesize = bytesize
        self.__serial.parity = parity
        self.__serial.stopbits = stopbits
        self.__serial.timeout = timeout
        self.__serial.xonxoff = xonxoff
        self.__serial.rtscts = rtscts

    def get_serial(self) -> serial:
        return self.__serial
