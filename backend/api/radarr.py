import logging
import requests
import json
from backend import constants

logger = None
enabled = False
api = ""
host = ""
path_start = ""
path_end_q = ""
path_end_a = ""
update_frequency = 0

def initialize():
    global path_start, path_end_question, path_end_ampersand, logger
    path_start = host+"api"
    path_end_question = "?apikey="+api
    path_end_ampersand = "&apikey="+api
    logger = logging.getLogger(__name__)
    #Creates a request for Radarr to check the system status
    try:
        request = requests.get(path_start+constants.RADARR_SYSTEM_STATUS+path_end_question)
        if(request.status_code is not 200):
            raise Exception()
        getAllMovies()
    except:
        logger.error("Could not create a connection to Radarr (status code {}). Please check config.ini.".format(request.status_code))
        exit()

# Gets all movies from Radarr as a list of lists [tmdbId, movie name]
def getAllMovies():
    try:
        request = requests.get(path_start+constants.RADARR_MOVIES+path_end_question)
        if(request.status_code is not 200):
            raise Exception()
        movies = []
        for movie in request.json():
            movies.append([movie['tmdbId'], movie['title']])
        return movies
    except:
        logger.error("Could not fetch series list from Radarr (status code {}).".format(request.status_code))

# Returns a JSON object with the series information
def getMovieInfo(id):
    try:
        request = requests.get(path_start+constants.RADARR_MOVIES_LOOKUP+str(id)+path_end_ampersand)
        if(request.status_code is not 200):
            raise Exception()
        return(request.json())
    except:
        logger.error("Could not fetch series info from Radarr (status code {}).".format(request.status_code))