# -*- coding:UTF-8 -*-

import os
from flask import Flask, Blueprint
from flask_restful import Api
from .config import get_config,configs
from .dependency import db
from . import Views
from . import Models

ALL_RESOURCE = [getattr(Views, x) for x in dir(Views)
                if x[:1].isupper() and
                hasattr(x, "url")]

def create_app(config = None):
    #create app
    app = Flask(__name__)

    #load config
    config = get_config(config)
    app.config.from_object(config)

    db.init_app(app)

    #load all api
    config_api(app)

    return app

def config_api(app):
    api = Api(app)

    for x in ALL_RESOURCE:
        api.add_resource(x, x.url)

