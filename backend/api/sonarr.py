from backend import logger, constants
import requests
import json

enabled = False
api = ""
host = ""
update_frequency = 0

def initialize():
    #Creates a request for Sonarr to check the system status
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.SONARR_SYSTEM_STATUS, params=payload)
        if(request.status_code is not 200):
            raise Exception()
    except:
        logger.error(__name__, "Could not create a connection to Sonarr: Please check config.ini")
        exit()

# Gets all shows from Sonarr as a list of lists [tvdb_id, show name]
def getAllShows():
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.SONARR_SERIES, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        shows = []
        for show in request.json():
            shows.append([show['tvdbId'], show['title']])
        return shows
    except:
        logger.warning(__name__, "Could not fetch series list from Sonarr (status code {})".format(request.status_code))

def getAllShowIDs():
    try:
        payload = {'apikey': api}
        request = requests.get(host+constants.SONARR_SERIES, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        shows = []
        for show in request.json():
            shows.append(show['tvdbId'])
        return shows
    except:
        logger.warning(__name__, "Could not fetch series list from Sonarr (status code {})".format(request.status_code))


# Returns a JSON object with the series information
def getShowInfo(id):
    try:
        payload = {'term': 'tvdb:'+str(id),'apikey': api}
        request = requests.get(host+constants.SONARR_SERIES_LOOKUP, params=payload)
        if(request.status_code is not 200):
            raise Exception()
        return(request.json())
    except:
        logger.warning(__name__, "Could not fetch series info from Sonarr (status code {})".format(request.status_code))