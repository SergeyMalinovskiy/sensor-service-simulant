import requests
from abc import ABC
from requests import Response

from sensor_simulant.config.app_config import AppConfig


class GrowtherApi(ABC):
    def __init__(self, config: AppConfig):

        host = config.get_app_url()
        port = config.get_app_port()

        self._api_host = f'{host}:{port}/api/v1'


    def get_available_sensors(self) -> Response:
        return requests.get(f'{self._api_host}/sensors')
