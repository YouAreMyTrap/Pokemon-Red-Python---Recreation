import sqlite3
import hashlib
import os

class SQL:
    def __init__(self):
        if os.name == "nt":     # Windows
            slash = "\\"
        else:                   # Unix
            slash = "/"
        self.UserLogBD = os.path.dirname(os.path.realpath(__file__)) + slash + "chinook.db"

    def ConnectUser(self, name, passwd): 
        """Set name and password, if this correct return True or else return False"""
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        c.execute('SELECT * from Login WHERE name="%s" AND passw="%s"' % (name, hashlib.md5(passwd.encode('utf-8')).hexdigest()))
        if c.fetchone() == None:
            return False
        else:
            return True
        conn.close()

    def NewUser(self, name , passwd):
        """Set name and password, for create new user"""
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        c.execute("INSERT INTO Login (name, passw) VALUES ('%s', '%s')" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest())) 
        conn.commit()
        conn.close()

    def RemoveUser(self, name , passwd):
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        c.execute("DELETE FROM Login WHERE (name='%s' AND passw='%s')" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest())) 
        conn.commit()
        conn.close()
