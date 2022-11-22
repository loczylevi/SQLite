

import sqlite3

con = sqlite3.connect(':memory:')

cur = con.cursor()

class Adatbazis:
    def __init__(self,sor):
        orszag,datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[0:4])
        self.honap = datum[5:7]
        
with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
    fejlec = f.readline()
    data = [Adatbazis(sor) for sor in f]
cur.execute("DROP TABLE IF EXISTS eu")

cur.execute("""CREATE TABLE eu
        (orszag TEXT,
        datum TEXT,
        ev INTEGER,
        honap TEXT)
""")
for i in data:
    lista = [(i.orszag,i.datum,i.ev,i.honap)]
    cur.executemany("INSERT INTO eu VALUES (?,?,?,?) ", lista)
    
con.commit()

msg = cur.execute("SELECT * FROM eu")

print(msg.fetchall())

for row in cur.execute("SELECT * FROM eu"):
    print(row)

#darab = cur.execute(" SELECT count() FROM  eu ")[0][0]     
#print( f'3. feladat: Elemek száma:{ darab } ' )