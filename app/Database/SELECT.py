from  flask import url_for
import pymysql
from . import Connect_MYSQL
import re

dbs = Connect_MYSQL()

def give_all(table_name,db=Connect_MYSQL()):
    c = db.cursor()

    sql = ("SELECT * FROM %s" % (table_name))
    c.execute (sql)
    r = c.fetchall()

    print (r)

    for s in r:
        print (s)
    #db.close()
    return r

def give_s_class(class_name,db=Connect_MYSQL()):
    c = db.cursor()
    sql = '''SELECT s.name FROM classes_second s\
            WHERE s.f_id = (\
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

'''def class_first_all (class_name,db=Connect_MYSQL()):
    c= db.cursor()
    sql = 'SELECT\
            s.name,\
            s.j_standard,\
            s.top_preface,\
            s.top_title,\
            s.medium_preface,\
            s.medium_title,\
            s.low_preface,\
            s.low_title\
            FROM classes_second s\
            WHERE s.f_id=\
            (SELECT\
            id\
            FROM classes_first\
            WHERE name='%s')' %\
            (class_name)
    c.execute(sql)
    r = c.fetchall()
    if r ==():
        return False
    d={}
    for n in list(range(len(r))):
        key ='class_'+str(n+1)
        d[key]= r[n]
    c.close()
    return d'''

def g_p_j (class_second_name,db = Connect_MYSQL):
    c = db.cursor()
    sql = '''SELECT\
            p.name,\
            p.level\
            FROM products p\
            WHERE p.s_id =\
            (SELECT\
            id\
            FROM classes_second\
            WHERE name='%s')'''% \
            (class_second_name)

    c.execute(sql)
    r = c.fetchall()

    if r == () :
        return False

    sql = '''SELECT s.j_standard j\
            FROM classes_second s\
            WHERE s.name = '%s' '''%\
            (class_name)
    c.execute(sql)
    j = c.fetchall()

    if j == () :
        return False

    le ={}
    d = {"j_standard":j['j']}
    for n in list(range(len(r))):
        key = 'level_'+str(r[n]['level'])
        le[key]=r[n]['name']

    d['products']=le

    return d



'''def class_second_all (class_name,db=Connect_MYSQL()):
    c = db.cursor()
    sql = 'SELECT\
            p.name,\
            p.level\
            FROM products p\
            WHERE p.s_id =\
            (SELECT\
            id\
            FROM classes_second\
            WHERE name='%s')'% \
            (class_name)
    print (sql)
    c.execute(sql)
    r = c.fetchall()
    if r == () :
        return False
   
    d ={}
    for n in list(range(len(r))):
        key = 'level_'+str(r[n]['level'])
        d[key]=r[n]['name']
    #db.close()
    return d'''

def product_all (product_name,db=Connect_MYSQL()):
    c = db.cursor()
    
    sql = '''SELECT\
            p.name,\
            p.level,\
            p.price,\
            p.title,\
            p.commentaries\
            FROM products p\
            WHERE p.name='%s' ''' %\
            (product_name)
    print (sql)
    c.execute(sql)
    r = c.fetchall()
    if r == () :
        return False
    
    d=r[0]
    #db.close()
    return d

def give_c_id(class_name,db=Connect_MYSQL()):
    c= db.cursor()
    sql='''SELECT s.id\
            FROM classes_second s\
            WHERE s.name = '%s' '''%\
            (class_name)
    c.execute(sql)
    r = c.fetchall()
    r = r[0]['id']
    #db.close()
    
    return r

def g_p_id(product_name,db=Connect_MYSQL()):
    c = db.cursor()
    sql = '''SELECT p.id\
            FROM products p
            WHERE p.name = '%s' '''%\
            (product_name)
    c.execute(sql)
    print (c.rowcount)
    r = c.fetchall()
    if r == ():
        print (r)
    c.close()
    db.close()
    return r[0]['id']



