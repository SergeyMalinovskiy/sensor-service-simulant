from datetime import datetime

from libs.contract.python.data import SendData
from sensor_simulant.sensors.environment import MeasureEnvironment
from sensor_simulant.sensors.interface import FeelingEnvironment, ContainsMeasurementInfo
from sensor_simulant.sensors.sensor import Sensor


class BaseEnvironmentSensor(Sensor, FeelingEnvironment):
    def __init__(self, sensor_id, emitter, *args, **kwargs):
        self._environment: MeasureEnvironment | None = None

        super().__init__(sensor_id, emitter, *args, **kwargs)


    def immerse_to_environment(self, environment: MeasureEnvironment) -> None:
        self._environment = environment


    def _measure_environment(self) -> float:
        environment = self._environment

        if (environment is None) | (not isinstance(self, ContainsMeasurementInfo)):
            return 0

        return environment.get_data().get(self.get_measured_quantity(), 0)


    def _generate_data(self) -> SendData:
        value = str(self._measure_environment())

        return SendData(
            value=value,
            datetime=datetime.now(),
            comment="",
        )
