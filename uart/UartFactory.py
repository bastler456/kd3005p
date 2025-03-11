import json
from uart.UartSetup import UartSetup
from pathlib import Path


class UartFactory():
    @staticmethod
    def create_uart_setup(path: Path) -> UartSetup:
        with path.open('r') as file:
            uart_settings = json.load(file)
        port: str = uart_settings.get("port")
        baud: int = uart_settings.get("baud")
        bytesize: int = uart_settings.get("bytesize")
        parity: str = uart_settings.get("parity")
        stopbits: int = uart_settings.get("stopbits")
        timeout: int = uart_settings.get("timeout")
        xonxoff: int = uart_settings.get("xonxoff")
        rtscts: int = uart_settings.get("rtscts")
        return UartSetup(port,
                         baud,
                         bytesize,
                         parity,
                         stopbits,
                         timeout,
                         xonxoff,
                         rtscts)
