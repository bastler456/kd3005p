from uart.UartFactory import UartFactory
from uart.UartSetup import UartSetup
from uart.uart import Uart
from protocol.kd3005p import Kd500p
from pathlib import Path
import time

def main():
    print(f"Hello from kd3005p! current voltage is: {test}")


if __name__ == "__main__":
    path: Path = Path('uart/config/config_usb.json')
    uart_setup: UartSetup = UartFactory.create_uart_setup(path)
    serial: Uart = Uart(uart_setup)
    serial.send_line("VSET1:20.5")
    time.sleep(1)
    serial.send_line("VSET1?")
    test = serial.read_line()
    kd500p: Kd500p = Kd500p(serial)
    kd500p.set_output(1)
    kd500p.set_ocp(1)
    kd500p.get_status()

    main()
