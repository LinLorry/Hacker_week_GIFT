import re,os,json
from app.Database import INSERT,SELECT,Connect_MYSQL
import urllib.request
from Pa import gong,d_all

f = open('./static/all_url.txt')
dbi = Connect_MYSQL()
try:
    os.mkdir(os.path.join('.','static','Images'))
except:
    pass

#爬下商品的数据以及图片地址
while f.readline() != "":
    #读取文件中已准备好的产品名字，产品等级，产品二级类别，该产品的淘宝API
    try:
        p_n = f.readline().replace("\n","")
        p_l = int(f.readline().replace("\n",""))
        c_n =f.readline().replace("\n","")
        url =f.readline().replace("\n","")
    except:
        break
    
    #获取产品二级类别的id
    c_id = SELECT.give_c_id(c_n)

    #定义一个所有价格的list
    p_p =[]

    #获取API内的所有地址
    p_u = d_all.tb.g_u(url)
    #开始爬虫
    p_a = gong.p_all(p_u)
    n=1

    #输出产品信息
    print ("====================================================================")
    print (p_n)
    print (p_l) 
    print (c_n)
    print (url)
    
    #逐个输出产品的最高价和最低价，如果没有则输出价格
    for p_o in p_a:
        print ("----------------------------------------")

        if po.p() == False:
            pass
        elif type(p_o.p()) == type(dict()):
            print ("H_price:%f\nL_price:%f"%(p_o.p()['H_price'],p_o.p()['L_price']))
            p_p.append(p_o.p()['H_price'])
            p_p.append(p_o.p()['L_price'])
        else:
            print ('pricce:%f'%p_o.p())
            p_p.append(p_o.p())
    
    #对所有价格进行判断，排除价格差太大的价格
    p_p=gong.pai(p_p)

    d_path = os.path.join('.','static','Images',c_n)
    try:
        #为每个二级产品创建一个文件夹
        os.mkdir(d_path)
    except:
        pass

    #插入产品数据
    INSERT.INSERT_prouduct(c_id,p_n,p_l,p_p['H_price'],p_p['L_price'],db=dbi)
    #打开一个文件存放图片地址
    fi = open (os.path.join(d_path,p_n+'.txt'),'a')
    for p_o in p_a:
        i_a = p_o.i()
        for o in i_a:
            fi.write(o+'\n')
    
    fi.close()

dbi.close()
f.seek(0)
dbs = Connect_MYSQL()

#通过图片地址下载图片
while f.readline() != "":
    #读取产品名字与二级类别名
    try:
        p_n = f.readline().replace("\n","")
        f.readline()
        c_n =f.readline().replace("\n","")
        f.readline()
    except:
        break

    n=1
    #获取产品二级id和产品id
    c_id = SELECT.give_c_id(c_n,db=dbs)
    p_id = SELECT.g_p_id(p_n,db=dbs)
    try:
        os.mkdir(os.path.join('.','static','Images',c_n,p_id))
    except:
        pass
    d_path = os.path.join('.','static','Images',c_n)
    p_path = os.path.join('.','static','Images',c_n,p_id)

    #打开存放图片地址的文件
    fi = open (os.path.join(d_path,p_n+'.txt'),'r')

    print ("====================================================================")
    print (p_n)

    for url in fi.readlines():
        try :
            url = url.replace("\n","")
        except:
            pass
        
        print (url)
        hou = re.match('.*(\..*)',url)
        name = str(str(n)+hou.group(1))
        path=os.path.join(p_path,name)
        print (path)
        try:
            
            urllib.request.urlretrieve(url,path)
            n=n+1
        except:
            pass

    fi.close()