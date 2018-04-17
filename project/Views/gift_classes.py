from urllib import parse
from flask import request,jsonify
from flask_restful import Resource
import project

class Get_first_classes(Resource):
    url = "/class_first"
    def get(self):
        all_classes = project.Models.Class_first.query.all()
        return jsonify(status = 1)

    def post(self):
        pass

class Get_second_classes(Resource):
    url = "/class_second"
    def get(self):
        re = request.query_string.decode('utf-8')
        re = parse.parse_qs(re)
        try:
            first_class_name = re['class_name'][0]
        except:
            pass

        return jsonify(status = 1)


