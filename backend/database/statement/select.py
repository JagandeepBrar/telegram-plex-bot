import sqlite3
from backend import constants

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
    for admin in db_cursor.execute('SELECT * FROM users WHERE status = 0'):
        admins.append(admin[0])
    return admins

# Get the list of shows that are active in the database
def getDatabaseShows():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    shows = []
    for show in db_cursor.execute('SELECT * FROM shows'):
        shows.append([show[0], show[1]])
    return shows