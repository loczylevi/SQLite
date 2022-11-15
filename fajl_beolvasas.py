"""year;programming language;first name; last name of chief developer"""

import sqlite3

def sql(c, sql_parancs, *args):
    c.execute(sql_parancs, *args)
    return c.fetchall()

conn = sqlite3.connect('data.db')
c = conn.cursor()

sql(c, " DROP TABLE IF EXISTS tb ")
sql(c, """
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
        print(sor)
        sql(c, " INSERT INTO tb VALUES (?,?,?,?) ", ( ev, programming_language, first_name, last_name))
conn.commit()
