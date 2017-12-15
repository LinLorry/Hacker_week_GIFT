import json
from flask import Flask,request,Response,make_response
from werkzeug.datastructures import Headers
from . import API
from ..Database import SELECT
import random

@API.route('/<class_name>/',methods=['GET'])
def g_s_classes(class_name):
    r= SELECT.class_first_all(class_name)
    
    all_c_name = json.dumps(r)
    print (all_c_name)
    return all_c_name

@API.route('/<class_first_name>/<class_second_name>/',methods=['GET'])
def g_c_products(class_first_name,class_second_name):
    r=SELECT.class_second_all(class_second_name)
    
    l = random.randint(1,3)
    m = random.randint(4,6)
    t = random.randint(7,9)

    r['level_low']=r['leve_'+str(l)]
    r['level_middle']=r['level_'+str(m)]
    r['level_top']=r['level_'+str(t)]

    all_p_name = json.dumps(r)
    print (all_p_name)
    return all_p_name

@API.route('/<class_first_name>/<class_second_name>/<product_name>/',methods=['GET'])
def g_p_all(class_first_name,class_second_name,product_name):
    r = SELECT.product_all(product_name)
    p_all = json.dumps(r)
    print (p_all)
    return p_all
