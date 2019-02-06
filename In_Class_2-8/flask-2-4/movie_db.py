from flask import Flask
import getpass, pymysql, sys

app = Flask(__name__)
app.db = None

def connect_db():
    if not app.db:
        db_IP = input('Inpute DB server IP address: ')
        pswd = getpass.getpass('Password: ')
        app.db = pymysql.connect(db_IP, 'root', pswd, 'films')
    else:
        print('Connected!', file=sys.stderr)

@app.route('/')
# Top-level route. Connects to DB if not already connected.
def hello():
    if not app.db:
        connect_db()

    return '<h1>' 'Welcome to the movie DB.' '</h1>'

@app.route('/all_movies')
def get_movies():
    if not app.db:
        connect_db()


    #retriving all the movies (a tuple of tuples)
    c = app.db.cursor()
    c.execute('SELECT * FROM movies')
    movie_list = c.fetchall()

    # using stdrr to output to terminal on VM
    print(movie_list, file=sys.stderr)
    movies = '<h2>'


    # convert movie tuples into a giant string to return in browser
    for movie in movie_list:
        movies += movie[0] + ' ' + str(movie[1]) + ' ' + str(movie[2]) + '<br>'
    movies += '</h2>'

    #show movies in broswer
    return movies

@app.route('/add_movie/<movie>')
def add_movie(movie):
    # assuming for corret format movie name:year:rating

    if not app.db:
        connect_db()

        #remove colon 
        toks = movie.split(':')

        c = app.db.cursor()

        query = 'INSERT INTO movies values("{}", {}, {});'.format(
                toks[0], toks[1], toks[2])

        print(query, file=sys.stderr)
        c.execute(query)

        app.db.commit()

        return '<h1>Record added </h2>'

@app.route('/rating/<rate>/')
def movie_rate(rate):
    
    if not app.db:
        connect_db()

    num = int(rate)

    c = app.db.cursor()
    c.execute('SELECT * FROM movies WHERE rating = %s', (num))
    ratings_list = c.fetchall()


    ratings = '<h2>'

    for num in ratings_list:
        ratings += num[0] + ' ' + str(num[1]) + ' ' + str(num[2]) + '<br>'
    ratings += '</h2>'

    return ratings











