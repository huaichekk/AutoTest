import pymysql
from pymysql.cursors import DictCursor




class MysqlConnection:
    def __init__(self,host,port,user,password,db):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset="utf8mb4",
            cursorclass=DictCursor,
            autocommit=True
        )
    def query(self,sql,params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql,params or ())
            return cursor.fetchall()

    def delete(self,sql,params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql,params or ())
            return cursor.rowcount

    def insert(self,sql,params=None):
        with self.conn.cursor() as cursor:
            return cursor.execute(sql,params or ())
conn = MysqlConnection('124.70.56.84',3306,'root','320930','netdisk')