import json
import logging

from app import configuration
from app.configuration import config


def detect_temperature():
    logging.info("Checking temperature and temperature")

    client = configuration.get_mqtt_client()
    client.connect()

    temp_message = "17,4 C"
    client.publish(config.MQTT_TOPIC_TEMPERATURE, temp_message)

    humidity_message = "86 %"
    client.publish(config.MQTT_TOPIC_HUMIDITY, humidity_message)

    client.disconnect()
