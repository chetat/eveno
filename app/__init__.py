""""
Main application directory module
"""
import os
from flask import Flask, jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv
from pathlib import Path

sqlalchemy = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

config = Config()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def create_app(config_obj=None):
    app = Flask(__name__)
    if config_obj is None:
        app.config.from_object(config)
    else:
        app.config.from_object(config_obj)
    initialize_extentions(app)
    register_blueprints(app)

    # This block below has shown me something
    with app.app_context():
        sqlalchemy.create_all()
    return app


def initialize_extentions(app):
    bcrypt.init_app(app)
    jwt.init_app(app)
    sqlalchemy.init_app(app)
    migrate.init_app(app, sqlalchemy)


def register_blueprints(app):
    from app.api import api
    app.register_blueprint(api)
