import sqlite3
con = sqlite3.connect(":memory:")

#year;programming language;first name; last name of chief developer

cur = con.cursor() # --> con olyan mint with open

cur.execute("DROP TABLE IF EXISTS nyelvek;")

cur.execute("CREATE TABLE nyelvek(year, programming_language,first_name,last_name_of_chief_developer)")


cur.execute("""
    INSERT INTO nyelvek VALUES
        (1972, 'C', 'Dennis', 'Ritchie'),
        (1964,'BASIC', 'John George', 'Kemeny'),
        (1964, 'BASIC', 'Thomas Eugene', 'Kurtz'),
        (1995, 'Java', 'James', 'Gosling'),
        (1983, 'C++', 'Bjarne', 'Stroustrup'),
        (1987, 'Perl', 'Larry', 'Wall'),
        (1995, 'JavaScript', 'Brendan','Eich'),
        (1970, 'Pascal', 'Niklaus', 'Wirth'),
        (1946, 'ENIAC Short Code', 'Richard', 'Clippinger'),
        (1946, 'ENIAC Short Code','John','von Neumann'),
        (1995, 'PHP','Rasmus','Lerdorf'),
        (1989, 'Python','Guido','Van Rossum'),
        (2000,'C#','Anders','Hejlsberg'),
        (1970, 'Pascal','Kathleen','Jensen')
        
""")


con.commit()

data = []
cur.executemany("INSERT INTO nyelvek VALUES(?, ?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

for row in cur.execute("SELECT * FROM nyelvek"):
    print(row)



    
con.close()



