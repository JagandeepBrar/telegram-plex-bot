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

# Get all the values from Sonarr
tvdb_id = environ.get('sonarr_series_tvdbid')
show_type = environ.get('sonarr_series_type')
show_title = environ.get('sonarr_series_title')
episode_title = environ.get('sonarr_episodefile_episodetitles')
season = environ.get('sonarr_episodefile_seasonnumber')
episode = environ.get('sonarr_episodefile_episodenumbers')
quality = environ.get('sonarr_episodefile_quality')
quality_version = environ.get('sonarr_episodefile_qualityversion')
download_time = datetime.datetime.utcnow().timestamp()
metadata_id = str(tvdb_id)+";"+str(constants.NOTIFIER_MEDIA_TYPE_TELEVISION)+";"+str(download_time)

# Insert the data into the metadata_television table in the database
db_cursor.execute("""INSERT OR IGNORE INTO metadata_television
    (metadata_id, tvdb_id, show_title, show_type, episode_title, season, episode, quality, quality_version, download_time)
    VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (metadata_id, tvdb_id, show_title, show_type, episode_title, season, episode, quality, quality_version, download_time))

# Commit the changes and close the database
db.commit()
db.close()

# Send the metadata_id to the bot so it can send out notifications
client_socket = socket.socket()
client_socket.connect((constants.SOCKET_HOST, int(constants.SOCKET_PORT)))
client_socket.send(metadata_id.encode('utf-8'))
client_socket.close()