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
    sum_p=0
    pd=re.match('(.*) \- (.*)',p)
    if (pd==None):
        sum_p=float(p)
        return sum_p
    else :
        l=[float(pd.group(1)),float(pd.group(2))]
        return pai(l)

def pai(l):

    if type(l) != type (list()):
        return l

    sum_p=0
    aver_p =l[0]
    a = len (l)

    for one in l:
        sum_p =sum_p+one

    aver_p=sum_p/a
    sum_p=0

    for n in list (range (a)):
        if l[n]<aver_p-aver_p/10:
            a=a-1
            continue
        sum_p = sum_p+l[n]


    aver_p=sum_p/a

    return aver_p
        
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
        
        print ('price:%f'%p.p())
        #print ('collect:%d'%p.c())
        p_a.append(p)

    return p_a








