import pyodbc
from services.utils import *


class Database(object):

    def __init__(self):
        try:
            q_str = "Driver={SQL Server};Server=20.228.144.215;port=1433;Network Library=DBMSSOCN;Database=Immilytics_IOP_V7;uid=sa;pwd=gskPraveen@123;"
            self._DB_Conn = pyodbc.connect(q_str)
            self._DB_Cur = self._DB_Conn.cursor()
            self._DB_Conn.autocommit = True
        except Exception as e:
            self._DB_Conn = False

    @property
    def DB_Conn(self):
        return self._DB_Conn

    @property
    def DB_Cur(self):
        return self._DB_Cur

    def executeOne(self, q, p=None):
        if not self._DB_Conn:
            return False, "Database is not available!", 404
        try:
            self._DB_Cur.execute(q, p) if p else self._DB_Cur.execute(q)
            result = self._DB_Cur.fetchone()
            dict_result = {} if not result else one_row_to_dict(result, self._DB_Cur.description)
            self._DB_Conn.close()
            if not dict_result:
                return False, "Record not found!", 204
            return True, dict_result, 200
        except Exception as e:
            print(e)
            self._DB_Conn.close()
            return False, "Bad Request", 400

    def executeAll(self, q, p=None):
        if not self._DB_Conn:
            return False, "Database is not available!", 404
        try:
            self._DB_Cur.execute(q, p) if p else self._DB_Cur.execute(q)
            result = self._DB_Cur.fetchall()
            dict_result = [] if not result else row_to_dict(result, self._DB_Cur.description)
            self._DB_Conn.close()
            if not dict_result:
                return False, "Record not found!", 204
            return True, dict_result, 200
        except Exception as e:
            print(e)
            self._DB_Conn.close()
            return False, "Bad Request", 400

    def queryOne(self, q, p=None):
        self.DB_Cur.execute(q, p) if p else self.DB_Cur.execute(q)
        result = self.DB_Cur.fetchone()
        result = {} if not result else one_row_to_dict(result, self.DB_Cur.description)
        return result

    def queryAll(self, q, p=None):
        self.DB_Cur.execute(q, p) if p else self.DB_Cur.execute(q)
        result = self.DB_Cur.fetchall()
        result = [] if not result else row_to_dict(result, self.DB_Cur.description)
        return result
