import re,json,requests,demjson
from . import gong

class tb:
    def __init__(self,b):
        self.b=b

    def g_u(url):
        p_url = []

        r = requests.get(url)
        r = r.text.replace('\n','')
        r = r.replace(' ','')
        ss = re.match(r'(.*)\((.*)\)(.*)',r)
        ss = ss.group(2)
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

    def i(self):
        f = self.b.find ('script',text=re.compile("auctionImages"))

        f = f.get_text()
        f = f.replace("\n","")
        f = f.replace(" ","")
        
        #f = re.match(r'.*idata.*?item.*?(\{.*?\}.*?\}).*',f)
        #f = re.match(r'(.*)disableAddToCart.*?\:.*?\,(.*)',f.group(1))
        f = re.match(r'.*(auctionImages.*?)\}.*',f)
        f = '{'+f.group(1)+'}'
        
        
        jo=demjson.decode(f)
        print (jo)
        
        
        i_u=[]
        for u in jo['auctionImages']:
            url = 'http:'+u
            i_u.append(url)
        
        return i_u

class tm:

    def __init__(self,b):
        self.b=b

    def g_u(url):
        pass

    def p(self):
        p_all = []
        c = self.b.find('script',text=re.compile("TShop.Setup"))

        s = c.get_text().replace('\n','')
        s = s.replace(' ','')
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

    def i(self):
        f = self.b.find('script',text=re.compile("TShop.Setup"))
        
        f = f.get_text().replace('\n','')
        f = f.replace(' ','')
        print (f)
        f = re.match(r'.*?propertyPics.*?(\"default\".*?)\}.*',f)
        f ='{'+f.group(1)+'}'
        print (f)
        jo = json.loads(f)
        i_u=[]
        for n in jo['default']:
            url = 'http:'+n
            print (url)
            i_u.append(url)
        
        return i_u



