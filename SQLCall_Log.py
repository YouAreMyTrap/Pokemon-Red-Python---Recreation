import sqlite3
import hashlib
import os

class SQL:
    def __init__(self):
        self.UserLogBD = os.path.dirname(os.path.realpath(__file__)) + "\chinook.db"

    def ConnectUser(self, name, passwd): 
        """Set name and password, if this correct return True or else return False"""
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        c.execute('SELECT * from Login WHERE name="%s" AND passw="%s"' % (name, passwd))
        if c.fetchone() == None:
            return False
        else:
            return True
        conn.close()

    def NewUser(self, name , passwd):
        print(hashlib.md5(passwd.encode('utf-8')).hexdigest())
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        #c.execute("INSERT INTO Users (name, pass) VALUES ('%s', %s)" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest())) 
        #c.commit()
        conn.close()
