from . import Connect_MYSQL

dbs = Connect_MYSQL()

def INSERT_prouduct(class_id,\
        name,\
        level,\
        price,\
        db=dbs):

    c = db.cursor()

    sql = '''INSERT products\
            (s_id,\
            name,\
            level,\
            price)\
            VALUES\
            (%d,'%s',%d,%d)'''%\
            (class_id,\
            name,\
            level,\
            price)
    print (sql)
    c.execute (sql)
    c.close()
    x=db.commit()
    
    return 0



