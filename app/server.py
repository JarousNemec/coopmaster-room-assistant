import logging

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from waitress import serve

from app import configuration
from app.blueprints.admin_blueprint import admin_blueprint
from app.configuration import config
from app.sensor.door_checker import DoorTimeChecker
from app.sensor.lamp_checker import LampTimeChecker

from app.cron.detect_hardware_state import detect_hardware_state


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        message = "Hello from room assistant!"
        logging.info(message)
        return message

    app.register_blueprint(admin_blueprint)

    return app


def server():
    manager_app = flask_app()

    LampTimeChecker(config.MQTT_TOPIC_LAMP_CMND)
    DoorTimeChecker(config.MQTT_TOPIC_DOOR_CMND)

    scheduler = BackgroundScheduler()
    scheduler.add_job(detect_hardware_state, 'interval', seconds=configuration.config.REPORT_INTERVAL, max_instances=1)
    scheduler.start()

    port = configuration.config.PORT
    host = configuration.config.HOST

    logging.info(f"Serving on http://{host}:{port}")
    serve(manager_app, port=port)
