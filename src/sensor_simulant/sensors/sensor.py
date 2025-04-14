from abc import ABC, abstractmethod

from libs.contract.python.data import SendData
from libs.contract.python.interface import SensorServiceEmitsData

_registered_sensor_ids = set()


class Sensor(ABC):
    def __init__(
            self,
            sensor_id: int,
            emitter: SensorServiceEmitsData,
            interval: int = 2,
            duration: int = None, # TODO: длительность измерений
    ) -> None:
        self._sensor_id = sensor_id
        self._emitter = emitter
        self._send_interval = interval

        self._prefix = "test"

        self._current_value = None
        self._duration = duration

    def send(self) -> int:
        data = self._generate_data()

        self._current_value = data.value

        print("Sensor {}: sending data..." . format(self._sensor_id))

        return self._emitter.send_data(self._sensor_id, data)

    def get_id(self) -> int:
        return self._sensor_id


    def get_interval(self) -> int:
        return self._send_interval


    def get_current_value(self) -> float:
        return self._current_value

    def get_duration(self) -> int:
        return self._duration


    @abstractmethod
    def _generate_data(self) -> SendData:
        pass
