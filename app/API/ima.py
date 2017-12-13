from flask import url_for,request,abort
from . import API
from ..Database import SELECT
import json

@API.route('/images/', methods=['POST'])
def get_qrcode():
    class_name = request.form.get ('class_name')
    name = request.form.get('name')
    print (type(class_name)) 
    if (type(class_name) != str\
            or type(name) != str):
        return abort(404)
    
    g=SELECT.image_name(class_name,name)
    if (g==False):
        return abort(404)
    im = json.dumps(g)

    return im

