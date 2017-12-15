import pymysql
import re,os,requests,json
from bs4 import BeautifulSoup
from app.Database import INSERT,SELECT
import urllib.request
from Pa import gong,d_all

#获取产品名字，评价,等级以及api路由
p_n = input ("input the name:")
#p_l = int(input("level:"))
c_n = input ('input the classname:')
#p_co = input("input the commentaries:")
c_id = SELECT.give_c_id(c_n)
url = input("input the url:")
p_sum=0
c_sum=0
p_p =[]
p_c =0
p_u = d_all.tb.g_u(url)
p_a = gong.p_all(p_u)
n=1

for p_o in p_a:
    p_p.append(p_o.p())

print ("----------------------------------------")
p_p = gong.pai(p_p)

print ('class_id:%d'%c_id)
print ('name:%s'%p_n)
print ('pricce:%f'%p_p)
#print ('collect:%d'%p_c)
#print ('com:%s'%p_co)

#INSERT.INSERT_prouduct(c_id,p_n,p_l,p_p,p_c,p_co)
p_id = SELECT.g_p_id(p_n)

try:
    os.mkdir(os.path.join('.','static','Images',c_n))
except:
    pass

for p_o in p_a:
    i_u = p_o.i()
    for u in i_u:
        hou = re.match('.*(\..*)',u)
        name = str(int(p_id))+'_'+str(n)+hou.group(1)
        print (u)
        path=os.path.join('.','static','Images',c_n,name)
        print(path)
        urllib.request.urlretrieve(u,path)
        n=n+1

