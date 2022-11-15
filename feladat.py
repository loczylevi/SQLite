import sqlite3
con = sqlite3.connect(":memory:")

#year;programming language;first name; last name of chief developer

cur = con.cursor() # --> con olyan mint with open

cur.execute("DROP TABLE IF EXISTS nyelvek;")

cur.execute("CREATE TABLE nyelvek(year, programming_language,first_name,last_name_of_chief_developer)")


cur.execute("""
    INSERT INTO nyelvek VALUES
        (1972, 'C', 'Dennis', 'Ritchie'),
        (1972, 'C', 'Dennis', 'Ritchie')
""")


con.commit()

data = [
    (1972, 'C', 'Dennis', 'Ritchie'),
    (1972, 'C', 'Dennis', 'Ritchie'),
    (1972, 'C', 'Dennis', 'Ritchie')
]
cur.executemany("INSERT INTO nyelvek VALUES(?, ?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

for row in cur.execute("SELECT year, programming_language FROM nyelvek ORDER BY year"):
    print(row)


print("______________________________________________________________________")
for row in cur.execute("SELECT year, programming_language FROM nyelvek"):
    print(row) 

    
con.close()



