# -*- coding:UTF-8 -*-

from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import get_config
from . import Views

db = SQLAlchemy()

ALL_RESOURCE = [getattr(Views, x) for x in dir(Views) if x[:1].isupper()]

def create_app(config = None):
    #create app
    app = Flask(__name__)

    #load config
    config = get_config(config)
    app.config.from_object(config)

    #use database
    db.init_app(app)

    #load all api
    config_api(app)

    return app

def config_api(app):
    api = Api(app)

    for x in ALL_RESOURCE:
        api.add_resource(x)

