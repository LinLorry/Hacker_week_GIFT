from  flask import url_for
import pymysql
from . import Connect_MYSQL,dbs
import re

#从一个MySQL表中获取所有内容的函数
#测试函数，不对返回值进行判断
def give_all(table_name,db=dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c = db.cursor()

    sql = ("SELECT * FROM %s" % (table_name))
    c.execute (sql)
    r = c.fetchall()

    print (r)

    for s in r:
        print (s)
    c.close()
    #db.close()
    return r

#以下是服务器的接口查询函数

#从产品二级类别表中查找一级产品为指定参数的所有二级产品
#class_name为一级类别名
#如果一级类别不存在，那么返回False
def give_s_class(class_name,db=dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c = db.cursor()
    sql = '''SELECT s.name FROM classes_second s
            WHERE s.f_id = (
            SELECT id FROM classes_first WHERE name = '%s')'''%\
            (class_name)
    
    c.execute(sql)
    r = c.fetchall()
    
    if r == ():
        return False
    
    d =  {}
    for n in list(range(len(r))):
        key = 'class_'+str(n+1)
        d[key] = r[n]['name']
    c.close()
    return d

#从产品表中查找二级产品为指定参数的所有产品名，产品等级，二级产品的划分依据
#class_name为二级产品名
#如果二级产品不存在，则返会False
def g_p_j (class_name,db = dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c = db.cursor()
    sql = '''SELECT
        p.name,
        p.level
        FROM products p
        WHERE p.s_id =
        (SELECT id
        FROM classes_second
        WHERE name ='%s') '''% \
        (class_name)

    c.execute(sql)
    r = c.fetchall()

    if r == () :
        return False

    sql='''SELECT j_standard j
            FROM classes_second s
            WHERE s.name = '%s' '''%\
            (class_name)
    
    c.execute(sql)
    j = c.fetchall()[0]

    le ={}

    d = {"j_standard":j['j']}
    for n in list(range(len(r))):
        key = 'level_'+str(r[n]['level'])
        le[key]=r[n]['name']
    
    d['products']=le
    c.close()

    return d

#将一个产品的详细信息返回
#返回有名字，等级，最高价，最低价，产品的标题，产品的评价
#如果该产品不存在则返回False
def product_all (product_name,db=dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c = db.cursor()
    
    sql = '''SELECT
            p.name,
            p.level,
            p.H_price,
            p.L_price,
            p.title,
            p.commentaries
            FROM products p
            WHERE p.name='%s' ''' %\
            (product_name)

    print (sql)
    c.execute(sql)
    r = c.fetchall()

    if r == () :
        return False

    #db.close()
    return r[0]

#以下是爬虫所需要的查询函数

#以二级类型名返回二级类型的id
#如果二级类型不存在则返回False
def give_c_id(class_name,db=dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c= db.cursor()

    sql='''SELECT s.id
            FROM classes_second s
            WHERE s.name = '%s' '''%\
            (class_name)

    c.execute(sql)
    r = c.fetchall()

    if r == () :
        return False
    c.close()

    return r[0]['id']

#以产品名返回产品的id
#如果产品不存在则返回False
def g_p_id(product_name,db=dbs):
    try:
        db.ping(True)
    except:
        dbs =Connect_MYSQL()
        db = db
    c = db.cursor()

    sql = '''SELECT p.id
            FROM products p
            WHERE p.name = '%s' '''%\
            (product_name)

    c.execute(sql)
    r = c.fetchall()

    if r == () :
        return False
    c.close()
   
    return r[0]['id']



