from os import environ, path
from backend import constants
import sqlite3
import datetime

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
download_time = datetime.datetime.now()
metadata_id = str(tmdb_id)+str(download_time.time())

# Insert the data into the metadata_movies table in the database
db_cursor.execute("""INSERT OR IGNORE INTO metadata_movies
    (metadata_id, tmdb_id, movie_title, quality, quality_version, download_time)
    VALUES
    (?, ?, ?, ?, ?, ?)
""", (metadata_id, tmdb_id, movie_title, quality, quality_version, download_time))

# Commit the changes and close the database
db.commit()
db.close()