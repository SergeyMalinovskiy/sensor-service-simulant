from abc import ABC, abstractmethod

from sensor_simulant.sensors.environment import MeasureEnvironment


class ContainsMeasurementInfo(ABC):
    @staticmethod
    @abstractmethod
    def get_measured_quantity() -> str:
        raise NotImplementedError()

#TODO: Наличие этого интерфейса может быть избыточно, переосмыслить!
# Датчик уже является зависимый от параметров окружения, так как их измеряет
# Однако, возможно будут случаи, когда сенсор может выступать в роли конвертора
class FeelingEnvironment(ABC):

    @abstractmethod
    def immerse_to_environment(self, environment: MeasureEnvironment) -> None:
        raise NotImplementedError()

    @abstractmethod
    def _measure_environment(self) -> float:
        raise NotImplementedError()
