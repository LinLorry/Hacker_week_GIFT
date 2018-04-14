import os
from os.path import abspath, join

def datapath(path):
    """相对于data目录的绝对路径"""
    return abspath(join("../data", path))

class Test:
    DEBUG = True
    DEBUG_LOG = datapath("debug.log")
    ERROR_LOG = datapath("error.log")

    SQLALCHEMY_DATABASE_URL = r'mysql://username:password@hostname/databse'
    SQLALCHEMY_TACK_MODIFICATIONS = True
class Product:
    DEBUG = True
    DEBUG_LOG = datapath("debug.log")
    ERROR_LOG = datapath("error.log")

    SQLALCHEMY_DATABASE_URL = os.environ.get("GIFT_DATABASE_URL")
    SQLALCHEMY_TACK_MODIFICATIONS = True

configs = {
    "Test":Test,
    "Product":Product
}

def get_config(name = None):
    return configs[name]