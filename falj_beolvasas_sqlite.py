"""year;programming language;first name; last name of chief developer"""

import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute(" DROP TABLE IF EXISTS tb ")
c.execute("""
    CREATE TABLE IF NOT EXISTS tb
    (ev        INTEGER,
    programming_language       TEXT,
    first_name    TEXT,
    last_name   TEXT)
""")
conn.commit()

with open('ize.txt', encoding='latin2') as f:
    fejlec = f.readline().strip()
    for sor in f:
        ev, programming_language, first_name, last_name  = sor.strip().split(';')
        print(sor,end="")
        c.execute(" INSERT INTO tb VALUES (?,?,?,?) ", ( ev, programming_language, first_name, last_name))
conn.commit()


