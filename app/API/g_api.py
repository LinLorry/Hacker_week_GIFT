import json,random
from flask import abort
from werkzeug.datastructures import Headers
from . import API
from ..Database import SELECT

#获取一级类别内的所有二级类别的接口
#class_name为一级类别名
#如果一级类别不存在，SELECT.give_s_class()会返回False
@API.route('/<class_name>/',methods=['GET'])
def g_s_classes(class_name):
    r= SELECT.give_s_class(class_name)

    if (r==False):
        return abort(404)

    all_c_name = json.dumps(r)
    return all_c_name

#获取二级类别内的所有产品以及该二级类别的划分说明的接口
#从产品中随机获取三种产品分为高中低
#class_first_name为一级类别名
#class_second_name为二级类别名
#如果二级类别不存在，SELECT.give_p_j()会返回False
@API.route('/<class_first_name>/<class_second_name>/',methods=['GET'])
def g_c_products(class_first_name,class_second_name):
    r=SELECT.g_p_j(class_second_name)
    if (r==False):
        return abort(404)
    
    l = random.randint(1,3)
    m = random.randint(4,6)
    t = random.randint(7,9)
    
    while (True):
        try:
            r['products']['level_low']=r['products']['level_'+str(l)]
            r['products']['level_middle']=r['products']['level_'+str(m)]
            r['products']['level_top']=r['products']['level_'+str(t)]
            break
        except:
            l = random.randint(1,3)
            m = random.randint(4,6)
            t = random.randint(7,9)

    
    all_p_name = json.dumps(r)
    return all_p_name

#获取产品的细节内容的接口
#class_first_name为一级类别名
#class_second_name为二级类别名
#product_name为产品名
#如果产品不存在，SELECT.product_all会返回False
@API.route('/<class_first_name>/<class_second_name>/<product_name>/',methods=['GET'])
def g_p_all(class_first_name,class_second_name,product_name):
    r = SELECT.product_all(product_name)

    if (r==False):
        return abort(404)

    p_all = json.dumps(r)
    return p_all
