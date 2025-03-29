import json

from libs.contract.python.data import ErrorData, SendData
from libs.contract.python.interface import SensorServiceEmitsData
from sensor_simulant.interface import Publisher


class Sensor(SensorServiceEmitsData):
    def __init__(self, sensor_id: int, publisher: Publisher) -> None:
        self.sensor_id = sensor_id
        self.publisher = publisher

        self.prefix = "test"


    def send_data(self, data: SendData) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{self.sensor_id}/data",
            data,
        )


    def send_ready(self) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{self.sensor_id}/ready",
            {},
        )


    def send_broken(self, error_data: ErrorData) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{self.sensor_id}/broken",
            error_data,
        )

