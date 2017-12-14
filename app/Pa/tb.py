import re,json,requests
from . import  gong
class tb():
    def __init__(self,b):
        self.b=b

    def p(self):
        f = self.b.find('em',class_='tb-rmb-num')
        f = gong.get_price(f.text)
        f = gong.pai(f)
        return f

    def c(self):
        f = self.b.find ('','')
        f = re.match(r'.*\((\d*)\).*',f)
        print (f.group(1))
        return f.group(1)

def g_u(url):
    p_url = []

    r = requests.get(url)
    ss = re.match(r'(\n\n.*)\((.*)\)(.*)',r.text)
    ss = ss.group(2)
    js = json.loads(ss)

    for jo in js['API.CustomizedApi']['itemlist']['auctions']:
        p_url.append('https:'+jo['detail_url'])
    
    return p_url

def tb_p(b):
    f = b.find('em',class_='tb-rmb-num')
    return gong.get_price(f.text)

def tb_c(b):
    return 0

def tb_i(b):
    i_a=[]
    return i_a

