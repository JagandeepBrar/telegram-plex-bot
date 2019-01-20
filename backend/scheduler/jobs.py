from backend.api import telegram, sonarr, radarr
from backend.scheduler.tasks import catalogue, notify
from backend import constants
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
        addRepeatingJob(catalogue.updateTelevision, constants.hoursToSeconds(sonarr.update_frequency))
    if(radarr.enabled):
        addRepeatingJob(catalogue.updateMovies, constants.hoursToSeconds(radarr.update_frequency))
    addRepeatingJob(notify.notifyDaily, constants.hoursToSeconds(24), notify.secondsToDaily())
    addRepeatingJob(notify.notifyWeekly, constants.daysToSeconds(7), notify.secondsToWeekly())

# Creates a repeating job, which will call <func> every <delay> seconds, with the first execution happening after <first> seconds
def addRepeatingJob(func, delay, first=0):
    job_queue.run_repeating(func, interval=delay, first=0)
    logger.info("Repeating job added to queue: {}, repeat delay: {}s, start delay: {}s".format(func.__name__, delay, first))

# Creates a single job, that will execute after <delay> seconds
def addSingleJob(func, delay, args):
    job_queue.run_once(func, delay, context=args)
    logger.info("Single job added to queue: {}, start delay: {}s".format(func.__name__, delay))
