from libs.contract.python.data import SendData, ErrorData
from libs.contract.python.interface import SensorServiceEmitsData
from sensor_simulant.interface import Publisher


class DataEmitter(SensorServiceEmitsData):
    def __init__(self, publisher: Publisher) -> None:
        self.publisher = publisher

        self.prefix = 'test'

    def send_data(self, sensor_id: int, data: SendData) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{sensor_id}/data",
            data,
        )

    def send_ready(self, sensor_id: int) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{sensor_id}/ready",
            {},
        )

    def send_broken(self, sensor_id: int, error_data: ErrorData) -> int:
        return self.publisher.publish(
            f"{self.prefix}/sensors/{sensor_id}/broken",
            error_data,
        )
