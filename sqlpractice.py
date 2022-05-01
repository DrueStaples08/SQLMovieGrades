# Import packages
import sqlite3

def create_db():
    # Create DB
    conn = sqlite3.connect('movies.db')
    # Create a cursor object which interacts with the DB i.e. SELECT, INSERT, etc.
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS MOVIES')
    cursor.execute('DROP TABLE IF EXISTS MOVIEINFO')
    # Create DB
    sql = '''
        CREATE TABLE MOVIES(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20) NOT NULL,
            ZIP_CODE INT, 
            TITLE CHAR(20) NOT NULL,
            GRADE INT
        )
            '''
    sql2 = '''
            CREATE TABLE MOVIEINFO(
            TITLE CHAR(20),
            YEAR INT, 
            GENRE CHAR(20)
        )
        '''
    cursor.execute(sql2)
    cursor.execute(sql)
    print('DB created successfully')
    conn.commit()
    conn.close()

def insert_db():
    conn = sqlite3.connect('movies.db')
    # Create a cursor object which interacts with the DB i.e. SELECT, INSERT, etc.
    cursor = conn.cursor()
    # Insert into DB
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Dade', 'Murphey', 55555, 'AntiTrust', 5)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Milo', 'Hoffman', 44444, 'The Empty Man', 4)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Dade', 'Murphey', 55555, 'You Wish', 2)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Milo', 'Hoffman', 44444, '3 Ninjas Knuckle Up', 0)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE) 
                    VALUES('Dade', 'Murphey', 55555, 'Alley Cat Strike', 5)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Milo', 'Hoffman', 44444, 'Get Out', 4)
                    ''')
    cursor.execute('''INSERT INTO MOVIES(FIRST_NAME, LAST_NAME, ZIP_CODE, TITLE, GRADE)
                    VALUES('Dade', 'Murphey', 55555, 'Willys Wonderland', 5)
                    ''')


    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('AntiTrust', 2001, 'Thriller')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('The Empty Man', 2020, 'Horror')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('You Wish', 2003, 'Kids and Family')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('3 Ninjas Knuckle Up', 1996, 'Kids and Family')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('Home Alone', 1992, 'Kids and Family')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('Turning Red', 2021, 'Kids and Family')
                    ''')
    cursor.execute('''INSERT INTO MOVIEINFO(TITLE, YEAR, GENRE)
                    VALUES('Just Friends', 2006, 'Romantic Comedy')
                    ''')
    #cursor.execute('''SELECT TITLE FROM MOVIES WHERE GENRE='Horror' ORDER BY TITLE''')
    print('Data Insertion Successful!')
    conn.commit()
    conn.close()

def select_db():
    # Create Connection to DB
    conn = sqlite3.connect('movies.db')
    # Create a cursor object which interacts with the DB i.e. SELECT, INSERT, etc.
    cursor = conn.cursor()
    # Retrieving Data
    #cursor.execute('SELECT * FROM MOVIES')

    # Use conditions to select from db
    #cursor.execute('SELECT TITLE FROM MOVIES WHERE GRADE >= 2')

    # Use "ORDER BY" to rearranege the order of a db by a column
    #cursor.execute('SELECT TITLE, GRADE FROM MOVIES ORDER BY GRADE')

    # Use "LIMIT" to retrieve data from a single row
    #cursor.execute("SELECT * FROM MOVIES LIMIT 2")


    # INNER JOIN
    # cursor.execute('''SELECT GRADE, YEAR, GENRE
    #                  FROM MOVIES
    #                  INNER JOIN MOVIEINFO
    #                  ON MOVIES.TITLE=MOVIEINFO.TITLE''')
    # cursor.execute('''SELECT GRADE, YEAR, GENRE
    #                  FROM MOVIES
    #                  INNER JOIN MOVIEINFO
    #                  USING(TITLE)''')
    # LEFT JOIN
    # cursor.execute('''SELECT TITLE, GRADE, YEAR, GENRE
    #                  FROM MOVIES
    #                  LEFT JOIN MOVIEINFO
    #                  USING(TITLE)''')
    # RIGHT JOIN - just switch MOVIES and MOVIEINFO
    # cursor.execute('''SELECT TITLE, GRADE, YEAR, GENRE
    #                  FROM MOVIEINFO
    #                  LEFT JOIN MOVIES
    #                  USING(TITLE)''')

    # FULL OUTER JOIN
    # cursor.execute('''SELECT TITLE, GRADE
    #                 FROM MOVIES
    #                 LEFT JOIN MOVIEINFO
    #                 USING(TITLE)
                    
    #                 UNION ALL

    #                 SELECT TITLE, GRADE
    #                 FROM MOVIEINFO
    #                 LEFT JOIN MOVIES
    #                 USING(TITLE)
    #                 ''')

    # # Another FULL OUTER JOIN EXAMPLE 
    # cursor.execute('''SELECT * FROM MOVIES
    #                 LEFT JOIN MOVIEINFO 
    #                 USING(TITLE)
                    
    #                 UNION ALL
                    
    #                 SELECT * FROM MOVIEINFO
    #                 LEFT JOIN MOIVES
    #                 USING(TITLE) ''')



    # CROSS JOIN
    cursor.execute('''SELECT * FROM MOVIES CROSS JOIN MOVIEINFO;''')


    # Fetching First Row from Table
    #print(cursor.fetchone())
    # Fetching All Rows from Table
    print(cursor.fetchall())
    # Fetch an n number of Rows
    #print(cursor.fetchmany(2))
    conn.commit()
    conn.close()

def update_db():
       conn = sqlite3.connect('movies.db')
       cursor = conn.cursor()
       update_sql_statement = '''UPDATE MOVIES SET GRADE=5 WHERE TITLE= '3 Ninjas Knuckle Up' '''
       cursor.execute(update_sql_statement)
       print('Table Updated')
       conn.commit()
       conn.close()

def delete_data():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE * FROM MOVIES WHERE TITLE LIKE '3 Ninjas' ''')
    conn.commit()
    conn.close()

def drop_table():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE MOVIES''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db()
    insert_db()
    select_db()
    # update_db()
    # select_db()

    #second_movie_db()