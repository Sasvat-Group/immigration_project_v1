from services.schemaServices import Database
from services.schemaServices.dbQuery import DBQuery


class UsersMaster:
    def getUsersDetailsByName(self, username):
        return Database().executeOne(DBQuery().GET_USER_DETAILS, (username,))
