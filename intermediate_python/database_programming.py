import sqlite3
connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS persons(
                first_name TEXT,
                last_name TEXT,
                age INTEGER
            )
               """)
cursor.execute("""
            INSERT INTO persons VALUES
            ('paul','smith',24),
            ('mark' , 'johnson',23),
            ('annah' , 'smith' , 32)
               """)
cursor.execute("""
               SELECT * FROM persons
               WHERE last_name = 'smith'
               """)
rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()