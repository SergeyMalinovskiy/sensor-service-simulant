import os
from abc import ABC

from dotenv import load_dotenv


class AppConfig(ABC):
    def __init__(self):
        load_dotenv()


    def get_mqtt_host(self) -> str:
        return os.getenv('MQTT_BROKER_HOST', 'localhost')


    def get_mqtt_port(self) -> int:
        return int(os.getenv('MQTT_BROKER_PORT', 1883))


    def get_app_url(self) -> str:
        return os.getenv('APP_URL', 'http://localhost:8080')


    def get_app_port(self) -> int:
        return int(os.getenv('APP_PORT', 8080))
