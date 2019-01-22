import sqlite3
from backend import constants

###############
# USERS TABLE #
###############

def deleteUser(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("PRAGMA foreign_keys = ON")
    db_cursor.execute('DELETE FROM users WHERE telegram_id = ?', (id,))
    db.commit()
    db.close()

###############
# SHOWS TABLE #
###############

def deleteTV(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("PRAGMA foreign_keys = ON")
    db_cursor.execute('DELETE FROM television WHERE tvdb_id = ?', (id,))
    db.commit()
    db.close()

################
# MOVIES TABLE #
################

def deleteMovie(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("PRAGMA foreign_keys = ON")
    db_cursor.execute('DELETE FROM movies WHERE tmdb_id = ?', (id,))
    db.commit()
    db.close()

###################
# NOTIFIERS TABLE #
###################

def deleteNotifier(id):
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    db_cursor.execute("PRAGMA foreign_keys = ON")
    db_cursor.execute('DELETE FROM notifiers WHERE watch_id = ?', (id,))
    db.commit()
    db.close()
