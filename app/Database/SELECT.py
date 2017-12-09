import pymysql
from . import Connect_MYSQL
import re

dbs = Connect_MYSQL()

def give_all(table_name,db=dbs):
    c = db.cursor()
    sql = ("SELECT * FROM %s" % (table_name))
    c.execute (sql)
    r = c.fetchall()

    for s in r:
        print (s)
    return r

def class_all (class_name,db=dbs):
    c = db.cursor()
    sql = '''SELECT\
            p.product_name name,\
            p.level\
            FROM products p JOIN classes_second s \
            ON s.class_name = '%s' ''' %\
            (class_name)
    print (sql)
    c.execute(sql)
    r = c.fetchall()
    d ={}
    for n in list(range(len(r))):
        key = 'leve_'+str(r[n]['level'])
        d[key]=r[n]['name']

    return d

def product_all (product_name,db=dbs):
    return 0
