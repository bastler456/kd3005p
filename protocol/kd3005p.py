from uart.uart import Uart


class Kd500p():
    def __init__(self, uart: Uart):
        self.__uart: Uart = uart

    def set_output_current(self, current: float, port: int = 1) -> None:
        command: str = f"ISET{port}:{current}"
        self.__uart.send_line(command)

    def get_output_current(self, port: int = 1) -> float:
        command: str = f"ISET{port}?"
        self.__uart.send_line(command)
        return self.__uart.read_line()

    def set_output_voltage(self, voltage: float, port: int = 1) -> None:
        command: str = f"VSET{port}:{voltage}"
        self.__uart.send_line(command)

    def get_output_voltage(self, port: int = 1) -> float:
        command: str = f"VSET{port}?"
        self.__uart.send_line(command)
        return self.__uart.read_line()

    def get_actual_output_current(self, port: int = 1) -> float:
        command: str = f"IOUT{port}?"
        self.__uart.send_line(command)
        return self.__uart.read_line()

    def get_actual_output_voltage(self, port: int = 1) -> float:
        command: str = f"VOUT{port}?"
        self.__uart.send_line(command)
        return self.__uart.read_line()

    def set_output(self, state: bool) -> None:
        command: str = f"OUT{int(state)}?"
        self.__uart.send_line(command)

    def get_status(self) -> dict:
        command: str = "STATUS?"
        self.__uart.send_line(command)
        response: str = self.__uart.read_line()
        if len(response) == 1:
            result: str = ord(response)
        elif len(response) == 4:
            filtered: str = response[2:4]
            result: int = int(filtered, 16)
        bitmask_mode: int = 1
        bitmask_ocp: int = 32
        bitmask_output: int = 64
        mode: int = result & bitmask_mode
        if mode == 0:
            mode_name = "CC mode"
        elif mode == 1:
            mode_name = "CV mode"
        else:
            raise IOError("unknown mode")
        ocp: int = result & bitmask_ocp == 32
        output: int = result & bitmask_output == 64
        result: dict = {"mode": mode_name,
                        "ocp": ocp,
                        "output": output}
        return result

    def get_identification(self) -> float:
        command: str = "*IDN?"
        self.__uart.send_line(command)
        return self.__uart.read_line()

    def set_ocp(self, state: bool) -> None:
        command: str = f"OCP{int(state)}"
        self.__uart.send_line(command)