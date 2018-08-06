from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()
db = MongoEngine()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    global stepic

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
