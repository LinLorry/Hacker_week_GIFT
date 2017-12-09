from flask import url_for
from . import API
import os
@API.route('/<class_name>/product_name/image/<image_name>', methods=['GET'])
def get_qrcode(class_name,product_name,image_name):

    return url_for('static',filename='Images/01.jpg')
