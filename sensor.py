import time
from datetime import datetime
from typing import Dict

import bme280
import smbus2

# BME280 sensor
port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)


def measuring_cycle(duration: int, freq: int) -> Dict:
    collected_data = {}

    for i in range(duration // freq):
        sensor_read = bme280.sample(bus, address, calibration_params)

        result = {"temperature": round(sensor_read.temperature, 1),
                  "pressure": round(sensor_read.pressure, 1),
                  "humidity": round(sensor_read.humidity, 2)}

        read_time = datetime.now().strftime("%H:%M:%S")
        collected_data.update({read_time: result})

        print({read_time: result})
        time.sleep(freq)

    return collected_data
