from Database import Connect_MYSQL

dbs = Connect_MYSQL()

def INSERT_prouduct(class_id,\
        product_id,\
        product_name,\
        level,\
        price,\
        collect_number,\
        commentaries,\
        db=dbs):

    c = db.cursor()

    sql = '''INSERT products\
            (class_id,\
            product_id,\
            product_name,\
            level,\
            price,\
            collect_number,\
            commentaries)\
            VALUES\
            (%d,%d,'%s',%d,%d,%d,'%s')'''%\
            (class_id,\
            product_id,\
            product_name,\
            level,\
            price,\
            collect_number,\
            commentaries)

    try:
        c.execute (sql)
        r =c.fetchall()
    except:
        return False

    return True
    
