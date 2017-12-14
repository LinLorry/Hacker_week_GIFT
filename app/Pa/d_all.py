import re,json,requests
from . import gong

class tb:
    def __init__(self,b):
        self.b=b

    def g_u(url):
        p_url = []

        r = requests.get(url)
        ss = re.match(r'(\n\n.*)\((.*)\)(.*)',r.text)
        ss = ss.group(2)
        print (ss)
        js = json.loads(ss)
    
        for jo in js['API.CustomizedApi']['itemlist']['auctions']:
            p_url.append('https:'+jo['detail_url'])
    
        return p_url

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

class tm:

    def __init__(self,b):
        self.b=b

    def p(self):
        p_all = []
        c = self.b.find('script',text=re.compile("TShop.Setup"))

        s=re.split('\n+',c.get_text())
        c=re.match(r'(.*)valItemInfo\"\:(.*\}\}\})',str(s))
        jo = json.loads(c.group(2))

        for n in list(range(len(jo['skuList']))):
            p_all.append(float(jo['skuMap']\
                    [';'+jo['skuList'][n]['pvs']+';'] \
                    ['price']))

        return gong.pai(p_all)

    def c(self):
        f = self.b.find ('','')
        f = re.match(r'.*\((\d*)\).*',f)
        print (f.group(1))
        return f.group(1)

