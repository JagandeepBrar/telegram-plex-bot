from backend.api import sonarr, radarr
from backend.database.statement import insert, select, delete
import logging

# Fetch all shows from Sonarr and update local database accordingly
def updateTelevision(bot, job):
    logger = logging.getLogger(__name__)
    logger.info("Updating television database...")
    shows = sonarr.getAllShows()
    if(shows is not None):
        # Add any new TV series to the database
        for show in shows:
            insert.insertTV(show[0], show[1])
        # Compare and delete removed shows from database to Sonarr
        shows_inactive = listDifference(shows, select.getDatabaseShows())
        if(len(shows_inactive) > 0):
            for show in shows_inactive:
                delete.deleteTV(show[0])
                logger.warning("Television series '{}' has been removed from the database.".format(show[1]))
        logger.info("Finished updating television database.")
    else:
        logger.error("Failed to update television database. Will try again at next scheduled run.")

# Fetch all movies from Radarr and update local database accordingly
def updateMovies(bot, job):
    logger = logging.getLogger(__name__)
    logger.info("Updating movies database...")
    movies = radarr.getAllMovies()
    if(movies is not None):
        # Add any new movies to the database
        for movie in movies:
            insert.insertMovie(movie[0], movie[1])
        # Compare and delete removed movies from database to Radarr
        movies_inactive = listDifference(movies, select.getDatabaseMovies())
        if(len(movies_inactive) > 0):
            for movie in movies_inactive:
                delete.deleteMovie(movie[0])
                logger.warning("Movie '{}' has been removed from the database.".format(movie[1]))
        logger.info("Finished updating movie database.")
    else:
        logger.error("Failed to update movie database. Will try again at next scheduled run.")

# Taken from https://www.geeksforgeeks.org/python-difference-two-lists/
def listDifference(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif