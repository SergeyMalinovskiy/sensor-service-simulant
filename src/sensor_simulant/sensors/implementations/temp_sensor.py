from sensor_simulant.sensors.base_environment_sensor import BaseEnvironmentSensor
from sensor_simulant.sensors.interface import ContainsMeasurementInfo

class TempCelsiusSensor(BaseEnvironmentSensor, ContainsMeasurementInfo):
    @staticmethod
    def get_measured_quantity() -> str:
        return "temperature"
