import pymysql
import re,os,requests,json
from bs4 import BeautifulSoup
from Database import INSERT,SELECT
import urllib.request
from Pa import gong,d_all

#获取产品名字，评价,等级以及api路由
p_n = input ("input the name:")
p_l = int(input("level:"))
c_n = input ('input the classname:')
p_co = input("input the commentaries:")
#p_n = '华为P10'
c_id = SELECT.give_c_id(c_n)
#print (c_id)

url = input("input the url:")
#url = "https://s.taobao.com/api?_ksTS=1513138752725_849&callback=jsonp850&ajax=true&m=customized&stats_click=search_radio_all:1&q=iPhonex&s=36&imgfile=&initiative_id=staobaoz_20171213&bcoffset=0&js=1&ie=utf8&rn=80535421298809b08bc5e23821ecb548"

p_sum=0
c_sum=0

p_p =[]
p_c =0

p_u = d_all.tb.g_u(url)
n=0

'''for url in p_u:
    ima = b.find_all('img',id = 'J_ImgBooth')

    for ima in i:
        #urllib.request.urlretrieve(ima,str(n)+'.jpg')
        n = n+1'''

p_a = gong.p_all(p_u)
p_p = []
for p_o in p_a:
    p_p.append(p_o.p())

print ("----------------------------------------")
p_p = gong.pai(p_p)

print ('class_id:%d'%c_id)
print ('name:%s'%p_n)
print ('pricce:%f'%p_p)
print ('collect:%d'%p_c)
print ('com:%s'%p_co)

INSERT.INSERT_prouduct(c_id,p_n,p_l,p_p,p_c,p_co)
#p = SELECT.product_all(p_n)
#print (p['product_name'])

