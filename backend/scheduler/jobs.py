from backend.api import telegram, sonarr, radarr
from backend.scheduler import catalogue
import time
import logging

job_queue = None
logger = None

def initialize():
    global job_queue, logger
    job_queue = telegram.updater.job_queue
    logger = logging.getLogger(__name__)
    logger.info("Job queue initialized")
    addDefaultJobs()

# Adds the default repeating tasks to the queue
def addDefaultJobs():
    logger.info("Adding default scheduler jobs")
    if(sonarr.enabled):
        addRepeatingJob(catalogue.updateTelevision, hoursToSeconds(sonarr.update_frequency))
    if(radarr.enabled):
        addRepeatingJob(catalogue.updateMovies, hoursToSeconds(radarr.update_frequency))


# Creates a repeating job, which will call <func> every <delay> seconds, with the first execution happening after <first> seconds
def addRepeatingJob(func, delay, first=0):
    job_queue.run_repeating(func, interval=delay, first=0)
    logger.info("Repeating job added to queue: {}, delay {}, first {}".format(func.__name__, delay, first))

# Creates a single job, that will execute after <delay> seconds
def addSingleJob(func, delay):
    job_queue.run_once(func, delay)
    logger.info("Single job added to queue: {}, delay {}".format(func, delay))

# Simple method to convert supplied hours to seconds
def hoursToSeconds(hours):
    return hours*3600