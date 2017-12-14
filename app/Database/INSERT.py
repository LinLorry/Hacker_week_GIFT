from . import Connect_MYSQL

dbs = Connect_MYSQL()

def INSERT_prouduct(class_id,\
        name,\
        level,\
        price,\
        collect_number,\
        commentaries,\
        db=dbs):

    c = db.cursor()

    sql = '''INSERT products\
            (s_id,\
            name,\
            level,\
            price,\
            collect_number,\
            commentaries)\
            VALUES\
            (%d,'%s',%d,%d,%d,'%s')'''%\
            (class_id,\
            name,\
            level,\
            price,\
            collect_number,\
            commentaries)
    print (sql)
    c.execute (sql)
    x=db.commit()
    print (x)
    r =c.fetchall()
    print ("3")
    
    return 0



