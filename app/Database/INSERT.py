from . import Connect_MYSQL,dbs

def INSERT_prouduct(class_id,\
        name,\
        level,\
        H_price,\
        L_price,\
        db=dbs):

    c = db.cursor()

    sql = '''INSERT products
            (s_id,name,level,H_price,L_price)
            VALUES
            (%d,'%s',%d,%d,%d)'''%\
            (class_id,\
            name,\
            level,\
            H_price,\
            L_price)

    c.execute (sql)
    c.close()
    db.commit()
    
    return 0



