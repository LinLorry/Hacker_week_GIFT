import os
from os.path import abspath, join

def datapath(path):
    """相对于data目录的绝对路径"""
    return abspath(join("./log", path))

class Config:
    @staticmethod
    def init_app(app):
        pass

class Test(Config):
    DEBUG = True
    DEBUG_LOG = datapath("debug.log")
    ERROR_LOG = datapath("error.log")

    SQLALCHEMY_DATABASE_URI = os.environ.get("GIFT_TEST_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    API_URL = "/test_api"

class Product(Config):
    DEBUG = False
    DEBUG_LOG = datapath("debug.log")
    ERROR_LOG = datapath("error.log")

    SQLALCHEMY_DATABASE_URI = os.environ.get("GIFT_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_URL = "/api"

configs = {
    "Test":Test,
    "Product":Product
}

def get_config(name = None):
    return configs[name]