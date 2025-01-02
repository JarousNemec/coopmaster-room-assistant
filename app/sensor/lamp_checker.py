import logging

from app import configuration
from app.sensor.driver_client import call_room_driver_command


class LampTimeChecker:

    def __init__(self, topic):
        self.mqtt_client = configuration.get_mqtt_client()
        self.topic = topic
        self.mqtt_client.connect()
        self.mqtt_client.set_topic(self.topic)
        self.mqtt_client.register_on_message_callback(self.process_on_message)

    def stop_checker(self):
        logging.info("Stopping checker")
        self.mqtt_client.close()

    def process_on_message(self, client, userdata, msg):
        logging.info(f"LampTimeChecker - Received message from topic {self.topic} : {msg.payload}")

        command = str(msg.payload.decode("utf-8"))
        payload = {"cmd": command}
        if command == "on":
            call_room_driver_command("lamp/on", payload)
        elif command == "off":
            call_room_driver_command("lamp/off", payload)
        else:
            logging.info(f"LampTimeChecker - invalid command: {command}")


