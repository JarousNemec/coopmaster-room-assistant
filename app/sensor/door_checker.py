import logging

from app import configuration
from app.sensor.checker import Checker
from app.sensor.driver_client import call_room_driver_command


class DoorTimeChecker(Checker):

    def process_on_message(self, client, userdata, msg):
        logging.info(f"DoorTimeChecker - Received message from topic {self.topic} : {msg.payload}")
        command = str(msg.payload.decode("utf-8"))
        payload = {"cmd": command}
        if command == "open":
            call_room_driver_command("door/open", payload)
        elif command == "close":
            call_room_driver_command("door/close", payload)
        else:
            logging.info(f"DoorTimeChecker - invalid command: {command}")



