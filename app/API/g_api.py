import json
from flask import Flask,request,Response,make_response
from werkzeug.datastructures import Headers
from . import API
from ..Database import SELECT

@API.route('/<class_name>/',methods=['GET'])
def g_s_classes(class_name):
    r= SELECT.class_first_all(class_name)
    
    all_c_name = json.dumps(r)
    print (all_c_name)
    return all_c_name

@API.route('/<class_first_name>/<class_second_name>/',methods=['GET'])
def g_c_products(class_first_name,class_second_name):
    r=SELECT.class_second_all(class_second_name)
    all_p_name = json.dumps(r)
    print (all_p_name)
    return all_p_name

@API.route('/<class_first_name>/<class_second_name>/<product_name>/',methods=['GET'])
def g_p_all(class_first_name,class_second_name,product_name):
    r = SELECT.product_all(product_name)
    p_all = json.dumps(r)
    print (p_all)
    return p_all
