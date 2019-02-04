from os import environ, path
from backend import constants
import sqlite3
import datetime
import socket

# Path to the database
db_path = path.realpath(path.dirname(path.realpath(__file__)))+"/"+constants.DB_FILE

#Open the connection to the database
db = sqlite3.connect(db_path)
db_cursor = db.cursor()

# Get all the values from Radarr
tmdb_id = environ.get('radarr_movie_tmdbid')
movie_title = environ.get('radarr_movie_title')
quality = environ.get('radarr_moviefile_quality')
quality_version = environ.get('radarr_moviefile_qualityversion')
if(environ.get('radarr_isupgrade') == "True"):
    is_upgrade = 1
else:
    is_upgrade = 0
download_time = datetime.datetime.utcnow().timestamp()
metadata_id = str(tmdb_id)+";"+str(constants.NOTIFIER_MEDIA_TYPE_MOVIE)+";"+str(download_time)

# Insert the data into the metadata_movies table in the database
db_cursor.execute("""INSERT OR IGNORE INTO metadata_movies
    (metadata_id, tmdb_id, movie_title, quality, quality_version, is_upgrade, download_time)
    VALUES
    (?, ?, ?, ?, ?, ?, ?)
""", (metadata_id, tmdb_id, movie_title, quality, quality_version, is_upgrade, download_time))

# Commit the changes and close the database
db.commit()
db.close()

# Send the metadata_id to the bot so it can send out notifications
client_socket = socket.socket()
client_socket.connect((constants.SOCKET_HOST, int(constants.SOCKET_PORT)))
client_socket.send(metadata_id.encode('utf-8'))
client_socket.close()