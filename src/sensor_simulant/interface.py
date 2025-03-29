from abc import abstractmethod, ABC

class Publisher(ABC):
    @abstractmethod
    def publish(self, channel: str, data: object) -> int:
        pass