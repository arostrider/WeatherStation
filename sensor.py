import time
from datetime import datetime, timedelta
from typing import Dict

import bme280
import smbus2

# BME280 sensor
port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)


def measuring_cycle(duration: int, time_step: int) -> Dict:
    """

    :param duration: seconds
    :param time_step: seconds
    :return: dict with temperature, pressure, and humidity data sampled after every time step over the cycle duration
    """
    collected_data = {}
    end_time = datetime.now() + timedelta(seconds=duration)

    while datetime.now() < end_time:
        sensor_read = bme280.sample(bus, address, calibration_params)

        result = {"temperature": round(sensor_read.temperature, 1),
                  "pressure": round(sensor_read.pressure, 1),
                  "humidity": round(sensor_read.humidity, 2)}

        read_time = datetime.now().strftime("%H:%M:%S")
        collected_data.update({read_time: result})

        print({read_time: result})
        time.sleep(time_step)

    return collected_data
