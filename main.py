import asyncio
import os
import random
import requests

from typing import Coroutine

from sensor_simulant import mqtt_publisher
from sensor_simulant.config.app_config import AppConfig

from sensor_simulant.data_emitter import DataEmitter
from sensor_simulant.sensors.environment import MeasureEnvironment
from sensor_simulant.sensors.interface import FeelingEnvironment
from sensor_simulant.sensors.sensor import Sensor
from sensor_simulant.sensors.implementations.temp_sensor import TempCelsiusSensor

_sensors: frozenset[Sensor] = frozenset([])
_measurement_environment: MeasureEnvironment = MeasureEnvironment()

def init_config() -> AppConfig:
    config = AppConfig()

    return config


async def main():
    global _sensors

    config = init_config()

    publisher = mqtt_publisher.MqttPublisher(config)
    emitter = DataEmitter(
        publisher
    )

    _sensors = frozenset([
        TempCelsiusSensor(1, emitter, 2),
        TempCelsiusSensor(2, emitter, 5),
    ])

    for sensor in _sensors:
        if isinstance(sensor, FeelingEnvironment):
            sensor.immerse_to_environment(_measurement_environment)

    await run_tasks()


async def send_data_task(sensor: Sensor):
    print("Sensor {}: start sending data with interval {} seconds".format(sensor.get_id(), sensor.get_interval()))

    while True:
        # delay = sensor.get_interval()
        sensor.send()
        #
        print("Sensor {}: sending data - {}".format(sensor.get_id(), sensor.get_current_value()))
        await asyncio.sleep(sensor.get_interval())


async def change_environment_task(environment: MeasureEnvironment):
    while True:
        print("Environment changed")

        environment.set_param('temperature', random.randint(16111, 18999) / 1000)

        print("Environment: {}".format(environment.get_data()))
        await asyncio.sleep(10)


async def prepare_task(coro: Coroutine):
    task = asyncio.create_task(coro)

    await task


async def run_tasks():
    tasks = [
        *[prepare_task(send_data_task(sensor)) for sensor in _sensors],
        prepare_task(change_environment_task(_measurement_environment)),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit(0)
