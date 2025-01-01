import json
import logging

from app import configuration
from app.configuration import config


def detect_temperature():
    logging.info("Checking temperature and temperature")

    client = configuration.get_mqtt_client()
    client.connect()
    temp_info = {"value": 17.0, "unit": "C"}
    temp_message = json.dumps(temp_info)
    client.publish(config.MQTT_TOPIC_TEMPERATURE, temp_message)

    humidity_info = {"value": 86.0, "unit": "%"}
    humidity_message = json.dumps(humidity_info)
    client.publish(config.MQTT_TOPIC_HUMIDITY, humidity_message)

    client.disconnect()
