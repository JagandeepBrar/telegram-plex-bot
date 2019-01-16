import sqlite3
import datetime
from backend import constants

###############
# USERS TABLE #
###############

# Update a user's data already in the database
def updateUser(telegram, status, frequency, detail, ombi, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ?, name = ?, status = ?, frequency = ?, detail = ? WHERE telegram_id = ?', (ombi, name, status, frequency, detail, telegram))
    db.commit()
    db.close()

# Update a user's status
def updateUserStatus(telegram, status):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET status = ? WHERE telegram_id = ?', (status, telegram))
    db.commit()
    db.close()

# Update a user's detail preference
def updateUserDetail(telegram, detail):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET detail = ? WHERE telegram_id = ?', (detail, telegram))
    db.commit()
    db.close()

# Update a user's frequency
def updateUserFrequency(telegram, frequency):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET frequency = ? WHERE telegram_id = ?', (frequency, telegram))
    db.commit()
    db.close()

# Update a user's ombi ID
def updateUserOmbi(telegram, ombi):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE users SET ombi_id = ? WHERE telegram_id = ?', (ombi, telegram))
    db.commit()
    db.close()

###############
# SHOWS TABLE #
###############

# Update a TV show's name that is already in the database
def updateTV(tvdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE shows SET name = ?, updated = ? WHERE tvdb_id = ?', (name, tvdb, datetime.datetime.now()))
    db.commit()
    db.close()

################
# MOVIES TABLE #
################

# Update a movie's name that is already in the database
def updateMovie(tmdb, name):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute('UPDATE movies SET name = ?, updated = ? WHERE tmdb_id = ?', (name, tmdb, datetime.datetime.now()))
    db.commit()
    db.close()
