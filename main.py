import time

from sensor_simulant import sensor, mqtt_publisher


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    publisher = mqtt_publisher.MqttSensorPublisher('localhost', 1883)

    try:
        publisher.loop_start()

        while True:
            publisher.subscribe(1)
            publisher.publish(1, "1234")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        publisher.stop()

    # sensor = sensor.Sensor(publisher, 1)
    #
    # sensor.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
