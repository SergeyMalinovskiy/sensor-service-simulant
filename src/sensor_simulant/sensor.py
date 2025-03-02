from sensor_simulant.interface import SensorPublisher


class Sensor:
    def __init__(self, publisher: SensorPublisher, sensor_id):
        self.publisher = publisher
        self.sensor_id = sensor_id


    def make(self, value):
        self.publisher.publish(self.sensor_id, value)
