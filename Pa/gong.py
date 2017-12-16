import re,requests
from bs4 import BeautifulSoup
from . import d_all

def pand_u(url):
    p = re.match ('(.*?)\.(.*?)\.(.*)',url)
    if p.group(2)=='taobao':
        return 0
    if p.group(2)=='tmall':
        return 1

def get_price(p):
    p = p.replace(" ","")
    pd=re.match('(.*) \- (.*)',p)
    if (pd==None):
        return float(pd)
    else :
        d = {"H_price":float(pd.group(2)),"L_price":float(pd.group(1))}
        return d

def pai(l):

    if type(l) != type (list()):
        return float(l)

    sum_p = 0
    a = len (l)

    for one in l:
        sum_p =sum_p+one

    aver_p=sum_p/a
    sum_p=0

    L_p=aver_p
    H_p=aver_p
    for n in list (range (a)):
        if l[n]<aver_p-aver_p/10:
            a=a-1
            continue
        if L_P>l[n]:
            l_P=l[n]
        if H_P<l[n]:
            H_P=l[n]
    
    d = {"H_price":float(pd.group(2)),"L_price":float(pd.group(1))}
        
    return d
        
def p_all(p_url):
    p_a = []
    for url in p_url:
        n = 1
        print ('--------------------------------------')
        print ('url:%s'%url)

        r = requests.get (url)
        b = BeautifulSoup (r.text,'html.parser')

        pd = pand_u(url)

        if pd == 0:
            p=d_all.tb(b)
        elif pd == 1:
            p=d_all.tm(b)
        else:
            p=None
            continue
        
        p_a.append(p)

    return p_a

def fen(l):
    if type(l) != type (list()):
        return l







