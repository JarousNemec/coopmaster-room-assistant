import logging

from app import configuration
from app.configuration import config
from app.sensor.driver_client import call_room_driver


def detect_hardware_state():
    logging.info("Checking temperature, humidity, door and lamp")

    client = configuration.get_mqtt_client()
    client.connect()
    try:
        temp_info = call_room_driver("temperature")
        client.publish(config.MQTT_TOPIC_TEMPERATURE, temp_info)

        humidity_info = call_room_driver("humidity")
        client.publish(config.MQTT_TOPIC_HUMIDITY, humidity_info)

        lamp_info = call_room_driver("lamp/state")
        client.publish(config.MQTT_TOPIC_LAMP_STATE, lamp_info)

        door_info = call_room_driver("door/state")
        client.publish(config.MQTT_TOPIC_DOOR_STATE, door_info)

    finally:
        client.disconnect()
