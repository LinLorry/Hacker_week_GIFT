import re,json

def tm_p (b):
     p_sum=0
     c=b.find('script',text=re.compile("TShop.Setup"))
     #x=b.find('div','p')
     #for xx in x:
     #  print (xx.get_text())

     s=re.split('\n+',c.get_text())

     c=re.match(r'(.*)valItemInfo\"\:(.*\}\}\})',str(s))

     jo = json.loads(c.group(2))
     for n in list(range(len(jo['skuList']))):
         p_sum = p_sum+float(jo['skuMap'][';'+jo['skuList'][n]['pvs']+';']['price'])
         aver = p_sum / len(jo['skuList'])
         return aver

def tm_c (b):
    c_sum=0

    f = b.find ('span',id='J_CollectCount')
    c_sum =int (f.get_text())

    return c_sum
  
def tm_i (b):
    ima = b.find_all('img',id = 'J_ImgBooth')
    i_a =[]
    for i in ima:
        i_a.append('http:'+i.get('src'))

    return i_a
