
#year;programming language;first name; last name of chief developer

import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

class Adatbazis:
    def __init__(self,sor):
        ev,nyelv,kereszt,vezetek = sor.strip().split(";")
        self.ev = int(ev)
        self.nyelv = nyelv
        self.kereszt = kereszt
        self.vezetek = vezetek
        
with open("ize.txt","r",encoding="latin2") as f:
    fejlec = f.readline()
    fejlec2 = f.readline()
    data = [Adatbazis(sor) for sor in f]
cur.execute("DROP TABLE IF EXISTS programozok")

cur.execute("""CREATE TABLE programozok
        (ev INTEGER,
        nyelv TEXT,
        kereszt TEXT,
        vezetek TEXT)
""")
for i in data:
    lista = [(i.ev,i.nyelv,i.kereszt,i.vezetek)]
    cur.executemany("INSERT INTO programozok VALUES (?,?,?,?) ", lista)
    
con.commit()

msg = cur.execute("SELECT * FROM programozok")

print(msg.fetchall())









    
        
        
