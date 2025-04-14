
class MeasureEnvironment():
    def __init__(self):
        self._params: dict[str, float] = {}

    def get_data(self) -> dict[str, float]:
        return self._params

    def set_param(self, key: str, value: float) -> None:
        self._params[key] = value
