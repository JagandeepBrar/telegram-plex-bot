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

# Get all user rows from 'users' table
def getUsers():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users')
    users = db_cursor.fetchall()
    db.commit()
    db.close()
    return users

# Get the 'users' table entries with the status code supplied
def getUsersWithStatus(status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE status = ?', (str(status),))
    users = db_cursor.fetchall()
    db.commit()
    db.close()
    return users

# Get the admins from the 'users' table
def getAdmins():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    admins = []
    for admin in db_cursor.execute('SELECT * FROM users WHERE status = ?', (constants.ACCOUNT_STATUS_ADMIN,)):
        admins.append(admin[0])
    db.commit()
    db.close()
    return admins

# Checks if the supplied user ID is registered
def isUserRegistered(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (id,))
    if(db_cursor.fetchone() is not None):
        db.commit()
        db.close()
        return True
    db.commit()
    db.close()
    return False

# Checks if the supplied user ID is <status>
def isUserStatus(id, status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM users WHERE telegram_id = ? AND status = ?', (id,status))
    if(db_cursor.fetchone() is not None):
        db.commit()
        db.close()
        return True
    db.commit()
    db.close()
    return False

###############
# SHOWS TABLE #
###############

# Get the list of shows that are active in the database
def getDatabaseShows():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    shows = []
    for show in db_cursor.execute('SELECT * FROM television'):
        shows.append([show[0], show[1]])
    return shows

# Get a tuple/row containing the information for the show matching the TVDB ID
def getShow(id):
    db = sqlite3.connect(constants.DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM television WHERE tvdb_id = ?', (id,))
    return db_cursor.fetchone()

def getShowByName(name):
    db = sqlite3.connect(constants.DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM television WHERE name = ?', (name,))
    return db_cursor.fetchone()

def getShowsSearch(text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM television WHERE name LIKE ?', ("%"+text+"%",))
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

def getMovieByName(name):
    db = sqlite3.connect(constants.DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM movies WHERE name = ?', (name,))
    return db_cursor.fetchone()

def getMoviesSearch(text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM movies WHERE name LIKE ?', ("%"+text+"%",))
    return db_cursor.fetchall()

##################
# NOTIFIER TABLE #
##################

def getNotifier(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM notifiers WHERE watch_id = ?', (id,))
    notifier = db_cursor.fetchone()
    db.commit()
    db.close()
    return notifier

def getNotifiers():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM notifiers')
    notifiers = db_cursor.fetchall()
    db.commit()
    db.close()
    return notifiers
    
def getNotifiersForUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM notifiers WHERE telegram_id = ?', (id,))
    notifiers = db_cursor.fetchall()
    db.commit()
    db.close()
    return notifiers

def getTelevisionNotifiersForUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM notifiers WHERE media_type = ?, telegram_id = ?', (constants.NOTIFIER_MEDIA_TYPE_TELEVISION, id))
    notifiers = db_cursor.fetchall()
    db.commit()
    db.close()
    return notifiers

def getMoviesNotifiersForUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('SELECT * FROM notifiers WHERE media_type = ?, telegram_id = ?', (constants.NOTIFIER_MEDIA_TYPE_MOVIE, id))
    notifiers = db_cursor.fetchall()
    db.commit()
    db.close()
    return notifiers

def getMoviesWatchedByUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM movies WHERE 
        tmdb_id IN (SELECT media_id FROM notifiers WHERE telegram_id = ? and media_type = ?)
    """, (id, constants.NOTIFIER_MEDIA_TYPE_MOVIE))
    movies = db_cursor.fetchall()
    db.commit()
    db.close()
    return movies

def getMoviesWatchedSearch(id, text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM movies WHERE 
        tmdb_id IN (SELECT media_id FROM notifiers WHERE telegram_id = ? and media_type = ?) AND
        name LIKE ?
    """, (id, constants.NOTIFIER_MEDIA_TYPE_MOVIE, "%"+text+"%"))
    movies = db_cursor.fetchall()
    db.commit()
    db.close()
    return movies

def getShowsWatchedByUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM television WHERE 
        tvdb_id IN (SELECT media_id FROM notifiers WHERE telegram_id = ? AND media_type = ?)
    """, (id, constants.NOTIFIER_MEDIA_TYPE_TELEVISION))
    shows = db_cursor.fetchall()
    db.commit()
    db.close()
    return shows

def getShowsWatchedSearch(id, text):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM television WHERE 
        tvdb_id IN (SELECT media_id FROM notifiers WHERE telegram_id = ? AND media_type = ?) AND
        name LIKE ?
    """, (id, constants.NOTIFIER_MEDIA_TYPE_TELEVISION, "%"+text+"%"))
    shows = db_cursor.fetchall()
    db.commit()
    db.close()
    return shows