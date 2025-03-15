from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import logging
from uart.UartFactory import UartFactory
from uart.UartSetup import UartSetup
from uart.uart import Uart
from protocol.kd3005p import Kd500p
from pathlib import Path
import time


app = Flask(__name__)
socketio = SocketIO(app, debug=True)

path: Path = Path('uart/config/config_usb.json')
uart_setup: UartSetup = UartFactory.create_uart_setup(path)
serial: Uart = Uart(uart_setup)
kd500p: Kd500p = Kd500p(serial)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/power', methods=['POST'])
def power():
    data: dict = request.get_json()
    mode: str = data.get("power")
    if mode == "Power ON":
        kd500p.set_output(1)
    elif mode == "Power OFF":
        kd500p.set_output(0)
    else:
        return 'bad request!', 400
    return 'ok!', 200


@app.route('/set', methods=['POST'])
def set():
    data: dict = request.get_json()
    voltage: float = float(data.get("voltage"))
    current: float = float(data.get("current"))
    if voltage > 0 and voltage < 31:
        if current >= 0 and current <= 5:
            kd500p.set_output_voltage(voltage)
            kd500p.set_output_current(current)
            return 'ok!', 200
    return 'bad request!', 400
        

socketio.run(app, '0.0.0.0', 8000, allow_unsafe_werkzeug=True)
