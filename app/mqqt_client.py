import logging

import paho.mqtt.client as mqtt


class NestMQTTClient:
    def __init__(self, broker, port, username, password):
        self.broker = broker
        self.port = port
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.username_pw_set(username, password)

    def set_topic(self, topic):
        self.mqtt_client.subscribe(topic)

    def connect(self):
        self.mqtt_client.connect(self.broker, self.port, 60)
        self.mqtt_client.loop_start()

    def publish(self, topic, payload):
        return self.mqtt_client.publish(topic, payload)

    def on_connect(self, client, userdata, flags, rc):
        pass

    # Definice callback funkce při přijetí zprávy
    def on_message(self, client, userdata, msg):
        pass

    def register_on_message_callback(self, method):
        self.mqtt_client.on_message = method

    def disconnect(self):
        self.mqtt_client.disconnect()
