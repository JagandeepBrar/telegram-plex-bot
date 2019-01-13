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

# Get the admins from the 'users' table
def getAdmins():
    db = sqlite3.connect(constants.DB_FILE)
    db_cursor = db.cursor()
    admins = []
    for admin in db_cursor.execute('SELECT * FROM users WHERE status = 0'):
        admins.append(admin[0])
    return admins
