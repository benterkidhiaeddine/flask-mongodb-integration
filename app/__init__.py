from flask import Flask
from settings import Config
from .api_v1 import api
from .main import main


def create_app(config_object=Config):
    app = Flask(__name__)

    app.config.from_object(config_object)

    # Extension initialization
    api.init_app(app)

    app.register_blueprint(main)

    return app
