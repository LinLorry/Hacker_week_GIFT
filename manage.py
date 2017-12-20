from flask import Flask
from app.API import API as API_blueprint
from flask_cors import *

app = Flask (__name__)

#BulePrint
app.register_blueprint(API_blueprint)
#解决跨域问题
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run (debug=True)
