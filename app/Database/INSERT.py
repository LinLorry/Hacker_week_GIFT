import pymysql
from config import Connect_MYSQL

xs = Connect_MYSQL()
db = xs.create_c()

class operation_mysql:
    def __init__(self,db):
        self.db = db

    def INSERT(self,table_name,data_name=None,data=None):
        c = self.db.cursor()
        sql = "INSERT INTO classes_first(class_name)VALUES('ss')"
        print (sql)
        try:
            print ('1')
            c.execute (sql)
            print ('2')
            c.commit()
            print ('3')
            return 0
        except:
            db.rollback()
            return 1

xx= operation_mysql(db)
print (xx.INSERT('classes_first','class_name','ss'))
db.close()
