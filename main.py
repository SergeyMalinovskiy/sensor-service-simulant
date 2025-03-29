import time
from datetime import datetime

from libs.contract.python.data import SendData
from sensor_simulant import mqtt_publisher
from sensor_simulant.sensor import Sensor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    publisher = mqtt_publisher.MqttPublisher('localhost', 1883)

    sensor = Sensor(1, publisher)
    try:
        publisher.loop_start()

        while True:
            data = SendData(
                value="1234",
                datetime=datetime.now(),
                comment="test data",
            )

            sensor.send_data(data)

            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        publisher.stop()

    # sensor = sensor.Sensor(publisher, 1)
    #
    # sensor.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
