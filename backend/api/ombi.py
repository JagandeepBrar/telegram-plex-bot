from backend import logger, constants
import requests
import json

enabled = False
api = ""
host = ""
update_frequency = 0

def initialize():
    try:
        payload = {'ApiKey': api}
        request = requests.get(host+constants.OMBI_SYSTEM_STATUS, params=payload)
        if(request.status_code is not 200):
            raise Exception()
    except:
        logger.error(__name__, "Could not create a connection to Ombi: Please check config.ini")
        exit()