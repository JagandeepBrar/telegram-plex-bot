from backend.api import sonarr, radarr
from backend.database.statement import insert, select, delete, update
from backend import constants, logger

# Fetch all shows from Sonarr and update local database accordingly
def updateTelevision(bot, job):
    logger.info(__name__, "Updating television database...")
    shows = sonarr.getAllShows()
    if(shows is not None):
        # Add any new TV series to the database
        for show in shows:
            insert.insertTV(show[0], show[1])
        # Compare and delete removed shows from database to Sonarr
        shows_inactive = constants.listDifference(select.getDatabaseShows(), shows)
        if(len(shows_inactive) > 0):
            show_ids = sonarr.getAllShowIDs()
            for show in shows_inactive:
                if(show[0] in show_ids):
                    update.updateTV(show[0], show[1])
                else:
                    delete.deleteTV(show[0])
                logger.warning(__name__, "Television series '{}' has been modified in the database".format(show[1]))
        logger.info(__name__, "Finished updating television database")
    else:
        logger.warning(__name__, "Failed to update television database. Will try again at next scheduled run")

# Fetch all movies from Radarr and update local database accordingly
def updateMovies(bot, job):
    logger.info(__name__, "Updating movies database...")
    movies = radarr.getAllMovies()
    if(movies is not None):
        # Add any new movies to the database
        for movie in movies:
            insert.insertMovie(movie[0], movie[1])
        # Compare and delete removed movies from database to Radarr
        movies_inactive = constants.listDifference(select.getDatabaseMovies(), movies)
        if(len(movies_inactive) > 0):
            movie_ids = radarr.getAllMovieIDs()
            for movie in movies_inactive:
                if(movie[0] in movie_ids):
                    update.updateMovie(movie[0], movie[1])
                else:
                    delete.deleteMovie(movie[0])
                logger.warning(__name__, "Movie '{}' has been modified the database".format(movie[1]))
        logger.info(__name__, "Finished updating movie database")
    else:
        logger.warning(__name__, "Failed to update movie database. Will try again at next scheduled run")
