import logging

from app import configuration


class LampTimeChecker:

    def __init__(self, topic):
        self.mqtt_client = configuration.get_mqtt_client()
        self.mqtt_client.set_topic(topic)
        pass

    def start_checker(self):
        logging.info("Checking lamp time")
        self.mqtt_client.register_on_message_callback(self.process_on_message)
        self.mqtt_client.connect()

    def stop_checker(self):
        logging.info("Stopping lamp time")
        self.mqtt_client.close()

    def process_on_message(self, client, userdata, msg):
        logging.info(f"LampTimeChecker - Received message from topic {userdata.topic}: {msg.payload}")
