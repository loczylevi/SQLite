import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor() # --> con olyan mint with open

cur.execute("DROP TABLE IF EXISTS movie;")

cur.execute("CREATE TABLE movie(title, year, score)")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")


con.commit()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)


print("______________________________________________________________________")
for row in cur.execute("SELECT year, title FROM movie WHERE year = 1982"):
    print(f"1982-es filmek: {row}") 

    
con.close()
