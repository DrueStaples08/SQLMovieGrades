# SQLMovieGrades
Includes a database program for grading movies and an easy go-to reference script for Sqlite3.

### Instatiate movie classes - attributes include title, grade, points, votes, and the mean score
antitrust = MovieGrade('AntiTrust', 'X', 0, 0, 0)

halloween = MovieGrade('Halloween', 'X', 0, 0, 0)

### Create database 
conn, cursor = db_connection()

create_db()

### Insert movies into database
insert_db(antitrust)

insert_db(halloween)

### Grade movies
grade_movie(usergrade('AntiTrust', 's'))

grade_movie(usergrade('Halloween', 'd'))

### View content from database
conn, cursor = db_connection()

view_movie_db()
