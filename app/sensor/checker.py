import logging

from app import configuration


class Checker:

    def __init__(self, topic):
        self.mqtt_client = configuration.get_mqtt_client()
        self.topic = topic
        self.mqtt_client.connect()
        self.mqtt_client.set_topic(self.topic)
        self.mqtt_client.register_on_message_callback(self.process_on_message)

    def stop_checker(self):
        logging.info("Stopping checker")
        self.mqtt_client.close()
