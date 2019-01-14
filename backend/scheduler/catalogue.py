from backend.api import sonarr
from backend.database.statement import insert
import logging

def updateTelevision(bot, job):
    logger = logging.getLogger(__name__)
    logger.info("Updating television database...")
    shows = sonarr.getAllShows()
    if(shows is not None):
        for show in shows:
            insert.insertTV(show[0], show[1])
        logger.info("Finished updating television database.")
    else:
        logger.error("Failed to update television database. Will try again at next scheduled run.")