import pymysql

def Connect_MYSQL():
    #数据库信息
    __host = 'localhost'
    __user = 'username'
    __pasw = 'password'
    __database = 'GIFT'

    return pymysql.connect (host=__host,\
            user=__user,\
            passwd=__pasw,\
            db=__database,\
            cursorclass = pymysql.cursors.DictCursor,\
            charset='utf8')


dbs=Connect_MYSQL()
