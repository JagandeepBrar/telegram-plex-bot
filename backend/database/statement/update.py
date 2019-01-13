import sqlite3
from backend import constants

###############
# USERS TABLE #
###############

# Update a user's data already in the database
def updateUser(telegram, ombi, status, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ?, name = ?, status = ? WHERE telegram_id = ?', (ombi, name, status, telegram))
    db.commit()
    db.close()

# Update a user's status
def updateUserStatus(telegram, status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET status = ? WHERE telegram_id = ?', (status, telegram))
    db.commit()
    db.close()

# Update a TV show's name that is already in the database
def updateTV(tvdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE shows SET name = ? WHERE tvdb_id = ?', (name, tvdb))
    db.commit()
    db.close()

# Update a movie's name that is already in the database
def updateMovie(tmdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE movies SET name = ? WHERE tmdb_id = ?', (name, tmdb))
    db.commit()
    db.close()
