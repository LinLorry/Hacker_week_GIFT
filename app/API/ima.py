from flask import url_for,request,abort,jsonify
from . import API
from ..Database import SELECT
import json,os

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
    l_dir = os.listdir(os.path.join('static','Images',data['class_name']))
    n=1
    for di in l_dir:
        
        url = url_for('static',filename=os.path.join('Images',\
                data['class_name'],di),_external=True)
        #url = url_for('static',filename=os.path.join(class_name,\
                #str(int(p_id))+'_'+str(n+1)))
        key='image_'+str(n+1)
        i_url[key]=url
        n=n+1

    #i_url = json.dumps(i_url)

    return jsonify(i_url)
