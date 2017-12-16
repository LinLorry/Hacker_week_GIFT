import pymysql
import re,os,requests,json
from bs4 import BeautifulSoup
from app.Database import INSERT,SELECT
import urllib.request
from Pa import gong,d_all

x=1
f = open('./static/all_url.txt')
r=1
while f.readline() != "":
    
    try:
        p_n = f.readline().replace("\n","")
        p_l = int(f.readline().replace("\n",""))
        c_n =f.readline().replace("\n","")
        url =f.readline().replace("\n","")
    except:
        break
    
    print ("====================================================================")
    print (p_n)
    print (p_l) 
    print (c_n)
    print (url)
    
    c_id = SELECT.give_c_id(c_n)
    
    p_p =[]
    p_c =0

    p_u = d_all.tb.g_u(url)
    p_a = gong.p_all(p_u)
    n=1

    for p_o in p_a:
        print ("----------------------------------------")

        if type(p_o.p()) == type(dict()):
            print ("H_price:%f\nL_price:%f"%(p_o.p()['H_price'],p_o.p()['L_price']))
            p_p.append(p_o.p()['H_price'])
            p_p.append(p_o.p()['L_price'])
        else:
            print ('pricce:%f'%p_o.p())
            p_p.append(p_o.p())
    
    p_p=gong.pai(p_p)

    try:
        d_path = os.path.join('.','static','Images',c_n)
        os.mkdir(d_path)
    except:
        pass

    if x==1:
        INSERT.INSERT_prouduct(c_id,p_n,p_l,p_p['H_price'],p_p['L_price'])
        fi = open (os.path.join(p_n+'.txt'),'a')
        for p_o in p_a:
            i_a = p_o.i()
            for o in i_a:
                fi.write(o+'\n')
    else:
        p_id = SELECT.g_p_id(p_n)
        fi = open (os.path.join(p_n+'.txt'),'r')
        for url in fi.readlines():
            try :
                url = url.replace("\n","")
            except:
                pass
            print (url)
            hou = re.match('.*(\..*)',url)
            name = str(int(p_id))+'_'+str(n)+hou.group(1)
            path=os.path.join('.','static','Images',c_n,name)
            print (path)
            urllib.request.urlretrieve(url,path)
            n=n+1
    
    fi.close()     

f.close()
