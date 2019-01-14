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

def initialize():
    global path_start, path_end_question, path_end_ampersand, logger
    path_start = host+"api"
    path_end_question = "?apikey="+api
    path_end_ampersand = "&apikey="+api
    logger = logging.getLogger(__name__)
    #Creates a request for Sonarr to check the system status
    try:
        request = requests.get(path_start+constants.SONARR_SYSTEM_STATUS+path_end_question)
        if(request.status_code is not 200):
            raise Exception()
    except:
        logger.error("Could not create a connection to Sonarr (status code {}). Please check config.ini.".format(request.status_code))
        exit()

# Gets all shows from Sonarr as a list of lists [tvdb_id, show name]
def getAllShows():
    try:
        request = requests.get(path_start+constants.SONARR_SERIES+path_end_question)
        if(request.status_code is not 200):
            raise Exception()
        shows = []
        for show in request.json():
            shows.append([show['tvdbId'], show['title']])
        return shows
    except:
        logger.error("Could not fetch series list from Sonarr (status code {}).".format(request.status_code))

# Returns a JSON object with the series information
def getShowInfo(id):
    try:
        request = requests.get(path_start+constants.SONARR_SERIES_LOOKUP+str(id)+path_end_ampersand)
        if(request.status_code is not 200):
            raise Exception()
        return(request.json())
    except:
        logger.error("Could not fetch series info from Sonarr (status code {}).".format(request.status_code))