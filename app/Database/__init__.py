import pymysql


def Connect_MYSQL():
    
    __host = 'localhost'
    __user = 'root'
    __pasw = 'password'
    __database = 'GIFT'

    return pymysql.connect (host=__host,\
            user=__user,\
            passwd=__pasw,\
            db=__database,\
            cursorclass = pymysql.cursors.DictCursor,\
            charset='utf8')
