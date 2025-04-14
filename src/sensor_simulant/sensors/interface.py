from abc import ABC, abstractmethod

from sensor_simulant.sensors.environment import MeasureEnvironment


class FeelingEnvironment(ABC):

    @abstractmethod
    def immerse_to_environment(self, environment: MeasureEnvironment) -> None:
        raise NotImplementedError()

    @abstractmethod
    def _measure_environment(self) -> float:
        raise NotImplementedError()
