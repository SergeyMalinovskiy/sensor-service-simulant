from datetime import datetime

from libs.contract.python.data import SendData
from libs.contract.python.interface import SensorServiceEmitsData
from sensor_simulant.sensors.environment import MeasureEnvironment
from sensor_simulant.sensors.interface import FeelingEnvironment
from sensor_simulant.sensors.sensor import Sensor

class TempCelsiusSensor(Sensor, FeelingEnvironment):
    def __init__(self, sensor_id: int, emitter: SensorServiceEmitsData, *args, **kwargs) -> None:
        self._environment: MeasureEnvironment = None

        super().__init__(sensor_id, emitter, *args, **kwargs)

    def _generate_data(self) -> SendData:
        value = str(self._measure_environment())

        return SendData(
            value=value,
            datetime=datetime.now(),
            comment="",
        )

    def immerse_to_environment(self, environment: MeasureEnvironment) -> None:
        self._environment = environment

    def _measure_environment(self) -> float:
        if self._environment is None:
            return 0
        return self._environment.get_data().get("temperature", 0)
