from backend.api import telegram, sonarr, radarr
from backend.scheduler.tasks import catalogue, notify
from backend import constants, logger
import time

job_queue = None

def initialize():
    global job_queue
    job_queue = telegram.updater.job_queue
    logger.info(__name__, "Job queue initialized")
    addDefaultJobs()

# Adds the default repeating tasks to the queue
def addDefaultJobs():
    logger.info(__name__, "Adding default scheduler jobs")
    if(sonarr.enabled):
        addRepeatingJob(catalogue.updateTelevision, constants.minutesToSeconds(sonarr.update_frequency))
    if(radarr.enabled):
        addRepeatingJob(catalogue.updateMovies, constants.minutesToSeconds(radarr.update_frequency))
    #addRepeatingJob(notify.notifyDaily, constants.hoursToSeconds(24), 0)
    addRepeatingJob(notify.notifyDaily, constants.hoursToSeconds(24), notify.secondsToDaily())
    addRepeatingJob(notify.notifyWeekly, constants.daysToSeconds(7), notify.secondsToWeekly())

# Creates a repeating job, which will call <func> every <delay> seconds, with the first execution happening after <first> seconds
def addRepeatingJob(func, delay, first=0):
    job_queue.run_repeating(func, interval=delay, first=first)
    logger.info(__name__, "Repeating job added to queue: {}, repeat delay: {}s, start delay: {}s".format(func.__name__, delay, first), "INFO_GREEN")

# Creates a single job, that will execute after <delay> seconds
def addSingleJob(func, delay, args):
    job_queue.run_once(func, delay, context=args)
    logger.info(__name__, "Single job added to queue: {}, start delay: {}s".format(func.__name__, delay), "INFO_GREEN")
