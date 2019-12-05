"""" 
Main application directory module
"""
from flask import Flask,jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

sqlalchemy = SQLAlchemy()

config = Config()
def create_app(config_obj=None):
    app = Flask(__name__)
    if config_obj is None:
        app.config.from_object(config)
    else:
        app.config.from_object(config_obj)
    initialize_extentions(app)
    register_blueprints(app)

    #This block below has shown me something
    with app.app_context():
        sqlalchemy.create_all()
    return app

def initialize_extentions(app):
    sqlalchemy.init_app(app)


def register_blueprints(app):
    from app.api import api
    app.register_blueprint(api)

