import sqlite3
import pandas as pd

class Database:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
    

    def createTableAndInsert(self, tableName, dataFrame):
        con = self.getConnection()
        dataFrame.to_sql(tableName, con, if_exists="replace", index=False)
        con.commit()
    
    def getConnection(self):
        return self.conn
