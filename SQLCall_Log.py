import sqlite3
import hashlib
class SQL:
    def __init__(self):
        self.UserLogBD = r"C:\Users\Pink\Documents\Pokemon-Red-Python---Recreation/chinook.db"

    def ConnectUser(self, name, passwd): 
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        c.execute("SELECT * FROM Login ") 
        print(c.fetchone())
        conn.close()

    def NewUser(self, name , passwd):
        print(hashlib.md5(passwd.encode('utf-8')).hexdigest())
        conn = sqlite3.connect(self.UserLogBD)
        c = conn.cursor()
        #c.execute("INSERT INTO Users (name, pass) VALUES ('%s', %s)" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest())) 
        #c.commit()
        conn.close()
