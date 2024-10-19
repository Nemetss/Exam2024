import mysql.connector
from flask import g, flash
from project.config import MysqlConfig

class MyDb:
    def __init__(self, app):
        self.app = app
        self.app.teardown_appcontext(self.close_db)

    def get_config(self):
        return {
            'user': MysqlConfig.MYSQL_USER,
            'password': MysqlConfig.MYSQL_PASSWORD,
            'host': MysqlConfig.MYSQL_HOST,
            'database': MysqlConfig.MYSQL_DATABASE,
        }

    def connect(self):
        if 'db' not in g:
            g.db = mysql.connector.connect(**self.get_config())
        return g.db


    def ExecuteQuery(self, query, params=[], query_type="get"):
        db = self.connect()
        cursor = db.cursor(named_tuple=True)
        try:
            cursor.execute(query, params)
            if query_type == "get":
                result = cursor.fetchall()
                print(result)
                return result
            else:
                db.commit()
                
        except mysql.connector.Error as err:
            flash(f"Error: {err}")
            db.rollback()
            return False
        finally:
            cursor.close()
           


 

    def close_db(self, e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()
