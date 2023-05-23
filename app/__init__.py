from flask import Flask 
from settings import Config
from .main import main
from .extensions import mongo



def create_app(config_object = Config):
    app = Flask(__name__)
    
    
    app.config.from_object(config_object)
    print(app.config)
    mongo.init_app(app)
    
    
    app.register_blueprint(main)

    return app


