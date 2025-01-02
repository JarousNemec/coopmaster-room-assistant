import logging

from app import configuration
from app.sensor.checker import Checker
from app.sensor.driver_client import call_room_driver_command


class LampTimeChecker(Checker):

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


