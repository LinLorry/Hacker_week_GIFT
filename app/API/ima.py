from flask import url_for,request,abort,jsonify
from . import API
from ..Database import SELECT
import json,os


#获取图片的API
#post信息内class_name为二类类别名name为产品名
#返回图片的地址
@API.route('/images/', methods=['POST'])
def get_qrcode():

    class_name = request.form.get('class_name')
    name = request.form.get('name')

    data = {}

    data['class_name']=class_name
    data['name']=name

    print (data['class_name'])
    print (data['name'])

    if (data['class_name'] == None\
            or data['name'] == None):
        return abort(404)
    
    p_id=SELECT.g_p_id(data['name'])
    if (p_id==False):
        return abort(404)

    i_url={}
    l_dir = os.listdir(os.path.join('static','Images',data['class_name'],str(p_id)))
    n=1
    for di in l_dir:
        
        url = url_for('static',filename=os.path.join('Images',\
                data['class_name'],str(p_id),di),_external=True)
        key='image_'+str(n+1)
        i_url[key]=url
        n=n+1

    #i_url = json.dumps(i_url)

    return jsonify(i_url)
