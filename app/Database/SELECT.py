from  flask import url_for
import pymysql
from . import Connect_MYSQL
import re

dbs = Connect_MYSQL()

def give_all(table_name,db=dbs):
    c = db.cursor()

    sql = ("SELECT * FROM %s" % (table_name))
    c.execute (sql)
    r = c.fetchall()

    print (r)

    for s in r:
        print (s)
    return r

def class_first_all (class_name,db=dbs):
    c= db.cursor()
    sql = '''SELECT\
            s.name\
            FROM classes_second s\
            WHERE s.f_id=\
            (SELECT\
            id\
            FROM classes_first\
            WHERE name='%s')''' %\
            (class_name)
    print (sql)
    c.execute(sql)
    r = c.fetchall()
    print (r)
    if r ==():
        return False
    d={}
    for n in list(range(len(r))):
        key ='class_'+str(n+1)
        d[key]= r[n]['name']
    return d

def class_second_all (class_name,db=dbs):
    c = db.cursor()
    sql = '''SELECT\
            p.name name,\
            p.level\
            FROM products p\
            WHERE p.s_id =\
            (SELECT\
            id\
            FROM classes_second\
            WHERE name='%s')'''% \
            (class_name)
    print (sql)
    c.execute(sql)
    r = c.fetchall()
    if r == () :
        return False
   
    d ={}
    for n in list(range(len(r))):
        key = 'leve_'+str(r[n]['level'])
        d[key]=r[n]['name']

    return d

def product_all (product_name,db=dbs):
    c = db.cursor()
    
    sql = '''SELECT\
            p.name,\
            p.level,\
            p.price,\
            p.collect_number,\
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
        
    return d

def give_c_id(class_name,db = dbs):
    c= db.cursor()
    sql='''SELECT s.id\
            FROM classes_second s\
            WHERE s.name = '%s' '''%\
            (class_name)
    c.execute(sql)
    r = c.fetchall()
    r = r[0]['id']

    return r

def g_p_id(product_name,db=dbs):
    c = db.cursor()
    sql = '''SELECT p.id\
            FROM products p
            WHERE p.name = '%s' '''%\
            (product_name)
    c.execute(sql)
    r = c.fetchall()
    return r[0]['id']


