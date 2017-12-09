import json
from flask import Flask,request,Response,make_response
from werkzeug.datastructures import Headers
from . import API
from ..Database import SELECT


class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)

@API.route('/<class_name>/',methods=['GET','POST'])
def g_c_products(class_name):
    r= SELECT.class_all(class_name)
    
    if request.method == 'GET':
        j_pr_name = json.dumps(r)
        print (j_pr_name)
        return j_pr_name
    else:
        a = make_response(str(r))
        #a.headers['Access-Control-Allow-Origin']='*'
        print  (type(a))
        return a
