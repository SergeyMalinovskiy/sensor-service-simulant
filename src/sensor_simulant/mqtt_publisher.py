import json
import time

from paho.mqtt import client as mqtt_client

from sensor_simulant.config.app_config import AppConfig
from sensor_simulant.interface import Publisher


class MqttPublisher(Publisher):
    def __init__(self, config: AppConfig):
        self._host = config.get_mqtt_host()
        self._port = config.get_mqtt_port()

        self.client = self._configure_client()


    def publish(self, channel: str, data: object) -> int:
        str_data = json.dumps(data.__dict__, indent=4, sort_keys=True, default=str)

        self.client.publish(channel, str_data)

        return 1


    def subscribe(self, sensor_id):
        self.client.subscribe(f"test/sensors/{sensor_id}")
        self.client.on_subscribe = self._on_subscribe


    def unsubscribe(self, sensor_id):
        self.client.unsubscribe(f"test/sensors/{sensor_id}")


    def _configure_client(self) -> mqtt_client.Client:
        client = mqtt_client.Client()

        client.on_connect = self._on_connect
        client.on_disconnect = self._on_disconnect
        client.connect(self._host, self._port, 60)
        time.sleep(2)


        return client


    def loop_start(self):
        self.client.loop_start()


    def stop(self):
        self.client.loop_stop()


    @staticmethod
    def _on_connect(client: mqtt_client.Client, userdata, flags, rc = None):
        print(f"Connected with result code {str(rc)}\n\n")
        client.publish('test', "Hello from Sensor Simulant!")


    @staticmethod
    def _on_disconnect(client: mqtt_client.Client, data, error):
        print(f"Client disconnected with result code {str(error)}\n")


    @staticmethod
    def _on_subscribe(client, userdata, mid, granted_qos):
        print(f"Data received!\n")

