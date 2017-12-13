import pymysql
import re,os,requests,json
from bs4 import BeautifulSoup
from Database import INSERT,SELECT
import urllib.request
from Pa import tm,tb

def pand_u(url):
    p = re.match ('(.*?)\.(.*?)\.(.*)',url)
    if p.group(2)=='tmall':
        return 0
    if p.group(2)=='taobao':
        return 1

def get_price(p):
    sum_p=0
    p=re.match('(.*) \- (.*)',p)
    if (p==None):
        sum_p=float(p)
    else :
        sum_p=(float(p.group(1))+float(p.group(2)))/2
    return sum_p

#获取产品名字，评价,等级以及api路由
p_n = input ("input the name:")
#p_l = int(input("level:"))
#p_co = input("input the commentaries:")

c_id = SELECT.give_c_id(p_n)
print (c_id)

#url = input("input the url:")
url = "https://s.taobao.com/api?_ksTS=1513138752725_849&callback=jsonp850&ajax=true&m=customized&stats_click=search_radio_all:1&q=iPhonex&s=36&imgfile=&initiative_id=staobaoz_20171213&bcoffset=0&js=1&ie=utf8&rn=80535421298809b08bc5e23821ecb548"
r =requests.get (url)


p_sum=0
c_sum=0


#将内容转化为python数据
ss = re.match(r'(\n\n.*)\((.*)\)(.*)',r.text)
ss = ss.group(2)
js = json.loads(ss)

p_u =[]

p_p =[]
p_c =[]

for n in list(range(len(js['API.CustomizedApi']['itemlist']['auctions']))):
    p_u.append('https:'+\
            js['API.CustomizedApi']\
            ['itemlist']\
            ['auctions']\
            [n]['detail_url'])

n=0

for url in p_u:
    print ('--------------------------------------------')
    print (url)

    r = requests.get (url)
    b = BeautifulSoup(r.text,'html.parser')
    ima = b.find_all('img',id = 'J_ImgBooth')
    
    if pand_u(url)==1:
        p = tb.tb_p(b)
        c = tb.tb_c(b)
        i = tb.tb_i(b)
    elif pand_u(url)==0:
        p = tm.tm_p(b)
        c = tm.tm_c(b)
        i = tm.tm_i(b)
    else :
        p ='no'

    for ima in i:
        #urllib.request.urlretrieve(ima,str(n)+'.jpg')
        n = n+1
    
    print ("price:%f"%p)
    print ("collect:%d"%c)
    p_p.append(p)
    p_c.append(c)
    


#INSERT(1,1,p_n,p_l,p_p,p_c,p_co)

