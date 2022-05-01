import sqlite3 
from moviegrade import MovieGrade



# Movie Grades 
grades_for_movies = {'S': 5.0, 'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0, 'X': 'NA'}



def usergrade(title, grade):
    return title, grade.upper() 



def db_connection():
    conn = sqlite3.connect('somemoviedb.db')
    cursor = conn.cursor()
    return conn, cursor



# Create Databaases
# Title, Grade (S, A, B, C, D, F, X), Total Points from cumulative grade scores, number of votes for each movie
def create_db():
    #conn, cursor = db_connection()
    cursor.execute("DROP TABLE IF EXISTS MOVIES")

    cursor.execute('''CREATE TABLE MOVIES 
                (TITLE TEXT, 
                GRADE TEXT, 
                POINTS INT, 
                VOTES INT, 
                MU REAL)
                ''')



def insert_db(movie):
    with conn:
        cursor.execute('''INSERT INTO MOVIES VALUES (?, ?, ?, ?, ? )''', (movie.title, movie.grade, movie.points, movie.votes, movie.mu))



def grade_movie(func):
    ititle, igrade = func
    cursor.execute(f"SELECT * FROM MOVIES where MOVIES.TITLE = ?", (ititle,))
    res = cursor.fetchall()
    #print(res)

    # Convert Grade (str) to Float Value (real)
    xtitle = res[0][0]
    xgrade = res[0][1]
    xpoints = res[0][2] 
    xvotes = res[0][3] + 1
    xmu = res[0][4]

    try: 
        new_grade_value = grades_for_movies[igrade]
        #print(f'new grade value {new_grade_value}')
    except KeyError:
        print('Grades need to be one of the following: S, A, B, C, D, F')

    xpoints += new_grade_value
    #print(xpoints, xvotes)

    xmu = xpoints / xvotes
    #print(xmu)

    if 4.5 <= xmu <= 5:
        xgrade = 'S'
    elif xmu >= 3.5:
        xgrade = 'A'
    elif xmu >= 2.5:
        xgrade = 'B'
    elif xmu >= 1.5:
        xgrade = 'C'
    elif xmu >= 0.5:
        xgrade = 'D'
    else:
        xgrade = 'F'
    #print(xgrade)

    # update 
    with conn:
        cursor.execute("UPDATE MOVIES SET GRADE = ?, POINTS = ?, VOTES = ?, MU = ? WHERE TITLE = ?", (xgrade, xpoints, xvotes, xmu, xtitle))

    print('DB updated successfully!')



def view_movie_db():
    with conn:
        cursor.execute("SELECT * FROM MOVIES")
        print(cursor.fetchall())
    # conn.commit()
    # conn.close()



if __name__ == '__main__':
    # First code block - run this to create db and insert movies 
    # Run the code block below ONLY ONCE
    # Run once to instantiate every movie as a class 
    # To add movies, insantiate the same as below just change the movie title
    antitrust = MovieGrade('AntiTrust', 'X', 0, 0, 0)
    halloween = MovieGrade('Halloween', 'X', 0, 0, 0)
    # Always run to establish the connection to db
    conn, cursor = db_connection()
    # Run once - no need to keep re-creating db unless we're testing out with ':memory' in ram instead of a db name in disk space
    create_db()
    # Run once to insert movie class into db
    insert_db(antitrust)
    insert_db(halloween)



    # Second code block - run this whenever you want to grade a movie
    # COMMENT OUT the code above then UNCOMMENT the code below to grade movies
    conn, cursor = db_connection()
    # Grade movie 
    grade_movie(usergrade('AntiTrust', 's'))
    grade_movie(usergrade('Halloween', 'd'))



    # Third code block - view the contents of the db 
    # Run whenenver you see fit - this prints out the current db so you can see your changes after grading
    conn, cursor = db_connection()
    view_movie_db()