import logging

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from waitress import serve

from app import configuration
from app.blueprints.admin_blueprint import admin_blueprint
from app.cron.check_lamp_time import check_lamp_time
from app.cron.dectect_temperature import detect_temperature
from app.cron.door_handler import check_door_handling_time


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

    scheduler = BackgroundScheduler()
    scheduler.add_job(check_lamp_time, 'interval', seconds=configuration.config.REPORT_INTERVAL)
    scheduler.add_job(detect_temperature, 'interval', seconds=configuration.config.REPORT_INTERVAL)
    scheduler.add_job(check_door_handling_time, 'interval', seconds=configuration.config.REPORT_INTERVAL)
    scheduler.start()


    port = configuration.config.PORT
    host = configuration.config.HOST

    logging.info(f"Serving on http://{host}:{port}")
    serve(manager_app, port=port)
