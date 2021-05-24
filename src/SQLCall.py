import sqlite3
import hashlib
import os


class SQL:
    def __init__(self):
        self.BD = os.path.normcase(os.path.dirname(os.path.realpath(__file__)) + "/chinook.db")

    def ConnectUser(self, name, passwd):
        """Set name and password, if this correct return True or else return False"""
        conn = sqlite3.connect(self.BD)
        c = conn.cursor()
        c.execute('SELECT * from Login WHERE name="%s" AND passw="%s"' % (name, hashlib.md5(passwd.encode('utf-8')).hexdigest()))
        if c.fetchone() is None:
            return False
        else:
            return True


    def NewUser(self, name , passwd):
        """Set name and password, for create new user"""
        conn = sqlite3.connect(self.BD)
        c = conn.cursor()
        c.execute('SELECT * from Login WHERE name="%s"' % (name))
        if c.fetchone() is None:
            c.execute("INSERT INTO Login (name, passw) VALUES ('%s', '%s')" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest()))
        else:
            return "user Already exist"
        conn.commit()
        conn.close()

    def RemoveUser(self, name , passwd):
        conn = sqlite3.connect(self.BD)
        c = conn.cursor()
        c.execute("DELETE FROM Login WHERE (name='%s' AND passw='%s')" %(name, hashlib.md5(passwd.encode('utf-8')).hexdigest()))
        conn.commit()
        conn.close()

    def CheckUser(self, name):
        conn = sqlite3.connect(self.BD)
        c = conn.cursor()
        c.execute("SELECT * from Login WHERE name='%s'" % (name))
        if c.fetchone() is None:
            return False
        else:
            return True
    def GetPokemon(self, id):
        conn = sqlite3.connect(self.BD)
        c = conn.cursor()
        c.execute("SELECT data from pokemon WHERE id=%s" % (id))
        #print(c.fetchone())
        #if c.fetchone() is not None: return c.fetchone()
        return c.fetchone()[0]# if c.fetchone() is None else c.fetchone()

