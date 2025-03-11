from uart.UartSetup import UartSetup
from uart.UartFilter import UartFilter
import logging


class Uart():
    def __init__(self, uartsetup: UartSetup) -> None:
        self.__serial = uartsetup.get_serial()
        self.__serial.open()

    def read_line(self) -> str:
        message: bytes = self.__serial.readline()
        logging.debug(f"received from uart: {message}")
        message_string: str = str(message)
        message_filtered: str = UartFilter.filter_message(message_string)
        return message_filtered

    def send_line(self, message: str) -> None:
        logging.debug(message)
        message = message + "\n"
        if not isinstance(message, bytes):
            message: str = message.encode('utf-8')
        logging.debug(f"send: {message}")
        self.__serial.write(message)
