import json,random
from flask import Flask,request,Response,make_response
from werkzeug.datastructures import Headers
from . import API
from ..Database import SELECT

@API.route('/<class_name>/',methods=['GET'])
def g_s_classes(class_name):
    r= SELECT.give_s_class(class_name)
    
    all_c_name = json.dumps(r)
    return all_c_name

@API.route('/<class_first_name>/<class_second_name>/',methods=['GET'])
def g_c_products(class_first_name,class_second_name):
    r=SELECT.g_p_jlass_second_name)
    
    l = random.randint(1,3)
    m = random.randint(4,6)
    t = random.randint(7,9)
    r['product']['level_low']=r['product'['level_'+str(l)]
    r['product']['level_middle']=r['product'['level_'+str(m)]
    r['product']['level_top']=r['product'['level_'+str(t)]

    all_p_name = json.dumps(r)
    return all_p_name

@API.route('/<class_first_name>/<class_second_name>/<product_name>/',methods=['GET'])
def g_p_all(class_first_name,class_second_name,product_name):
    r = SELECT.product_all(product_name)
    p_all = json.dumps(r)
    return p_all
