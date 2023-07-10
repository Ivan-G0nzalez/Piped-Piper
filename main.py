from flask import Flask, jsonify

from flask_restx import Api


from app.models.models import Components, Device
from app.models.exts import db
from flask_migrate import Migrate 

from app.namespaces.components import component_ns
from app.namespaces.devices import devices_ns
from app.namespaces.report import report_ns
from app.namespaces.threshold import threshold_ns
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException


from app.utils.logger import Logger

logger = Logger(__name__)

def create_app(config):
    logger.logger.info("Initializing the app")
    app = Flask(__name__)
    app.config.from_object(config)


    migrate=Migrate(app, db)
    

    api=Api(app,doc='/docs')
    api.add_namespace(component_ns)
    api.add_namespace(devices_ns)
    api.add_namespace(report_ns)
    api.add_namespace(threshold_ns)

    

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Components":Components,
            "devices":Device,
        }

    return app








