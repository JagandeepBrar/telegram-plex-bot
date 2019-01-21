import logging
import requests
import json

from colored import stylize
from backend import constants

logger = None
enabled = False
api = ""
host = ""
update_frequency = 0

def initialize():
    global logger
    logger = logging.getLogger(__name__)
    #Creates a request for Radarr to check the system status
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.RADARR_SYSTEM_STATUS, params=payload)
        if(request.status_code is not 200):
            raise Exception()
    except:
        logger.error(stylize("Could not create a connection to Radarr: Please check config.ini", constants.LOGGING_COLOUR_ERROR))
        exit()

# Gets all movies from Radarr as a list of lists [tmdbId, movie name]
def getAllMovies():
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.RADARR_MOVIES, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        movies = []
        for movie in request.json():
            movies.append([movie['tmdbId'], movie['title']])
        return movies
    except:
        logger.error("Could not fetch series list from Radarr (status code {}).".format(request.status_code))

# Gets all movies tmdb_ids from Radarr as a list
def getAllMovieIDs():
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.RADARR_MOVIES, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        movies = []
        for movie in request.json():
            movies.append(movie['tmdbId'])
        return movies
    except:
        logger.error("Could not fetch series list from Radarr (status code {}).".format(request.status_code))

# Returns a JSON object with the series information
def getMovieInfo(id):
    try:
        payload = {'tmdbId': str(id), 'apikey': api}
        request = requests.get(host+constants.RADARR_MOVIES_LOOKUP, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        return(request.json())
    except:
        logger.error("Could not fetch series info from Radarr (status code {}).".format(request.status_code))