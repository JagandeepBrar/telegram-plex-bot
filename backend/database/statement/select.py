import sqlite3
from backend import constants

###############
# USERS TABLE #
###############

# Gets the 'users' table entry for the supplied telegram ID
def getUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (str(id),))
    user = db_cursor.fetchone()
    db.commit()
    db.close()
    return user

# Get the 'users' table entries with the status code supplied
def getUsersWithStatus(status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE status = ?', (str(status),))
    return db_cursor.fetchall()

# Get the admins from the 'users' table
def getAdmins():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    admins = []
    for admin in db_cursor.execute('SELECT * FROM users WHERE status = ?', (constants.ACCOUNT_STATUS_ADMIN,)):
        admins.append(admin[0])
    return admins

# Checks if the supplied user ID is registered
def isUserRegistered(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (id,))
    if(db_cursor.fetchone() is not None):
        return True
    return False

# Checks if the supplied user ID is <status>
def isUserStatus(id, status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE telegram_id = ? AND status = ?', (id,status))
    if(db_cursor.fetchone() is not None):
        return True
    return False

###############
# SHOWS TABLE #
###############

# Get the list of shows that are active in the database
def getDatabaseShows():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    shows = []
    for show in db_cursor.execute('SELECT * FROM shows'):
        shows.append([show[0], show[1]])
    return shows

# Get a tuple/row containing the information for the show matching the TVDB ID
def getShow(id):
    db = sqlite3.connect(constants.DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM shows WHERE tvdb_id = ?', (id,))
    return db_cursor.fetchone()

def getShowsSearch(text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM shows WHERE name LIKE ?', ("%"+text+"%",))
    return db_cursor.fetchall()

################
# MOVIES TABLE #
################

# Get the list of movies taht are active in the database
def getDatabaseMovies():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    movies = []
    for movie in db_cursor.execute('SELECT * FROM movies'):
        movies.append([movie[0], movie[1]])
    return movies

# Get a tuple/row containing the information for the movie matching the TMDB ID
def getMovie(id):
    db = sqlite3.connect(constants.DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM movies WHERE tmdb_id = ?', (id,))
    return db_cursor.fetchone()

def getMovieSearch(text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM movies WHERE name LIKE ?', ("%"+text+"%",))
    return db_cursor.fetchall()
