import sqlite3


class Database:
    def __init__(self , db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bankinfo (id INTEGER PRIMARY KEY ,bank_name text , back_email text ,bank_pin text , bank_deposit int )")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM bankinfo")
        rows = self.cur.fetchall()
        return rows
    def insert(self , bank_name , bank_email , bank_pin , bank_deposit ):
        self.cur.execute("INSERT INTO bankinfo VALUES (NULL , ? , ? , ? , ?  )", (bank_name , bank_email , bank_pin , bank_deposit ))
        self.conn.commit()
    def remove(self , id):
        self.cur.execute("DELETE FROM bankinfo WHERE id=?" , (id,))
        self.conn.commit()
    def update(self, id ,bank_name , bank_email  , bank_pin , bank_deposit ):
        self.cur.execute("UPDATE bankinfo SET VALUES (? , ? , ? , ? ) WHERE id=?" , (bank_name , bank_email , bank_pin , bank_deposit , id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()
    def usernamefetch(self):
        self.cur.execute("SELECT( bank_name) FROM bankinfo")
        userow = self.cur.fetchall()
        return userow
    
    def passcodefetch(self , id):
        self.cur.execute("SELECT bank_pin FROM bankinfo WHERE id=?" ,(id,))
        pinrow = self.cur.fetchall()
        return pinrow
    def emailfetch(self):
        self.cur.execute("SELECT bank_email FROM bankinfo")
        emailrow = self.cur.fetchall()
        return emailrow
    def update_pin(self , id , bank_pin):
        self.cur.execute("UPDATE bankinfo SET bank_pin=? WHERE id=?", (bank_pin , id))
        self.conn.commit()
    def balancefetch(self , id):
        self.cur.execute("SELECT bank_deposit FROM bankinfo WHERE id=?" , (id,))
        balance_row = self.cur.fetchall()
        return balance_row
    def update_balance(self , id ,bank_balance):
        self.cur.execute("UPDATE bankinfo SET bank_deposit=? WHERE id=?" , (bank_balance , id))
        self.conn.commit()
        
        
db = Database("atmdb.db")
