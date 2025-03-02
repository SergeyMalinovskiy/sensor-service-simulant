from abc import ABC, abstractmethod

class SensorPublisher(ABC):
    @abstractmethod
    def publish(self, sensor_id, data):
        pass