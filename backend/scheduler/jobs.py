from backend.api import telegram
import time

job_queue = None

def initialize():
    global job_queue
    job_queue = telegram.updater.job_queue

# Creates a repeating job, which will call <func> every <delay> seconds, with the first execution happening after <first> seconds
def addRepeatingJob(func, delay, first=0):
    job_queue.run_repeating(func, interval=delay, first=0)

# Creates a single job, that will execute after <delay> seconds
def addSingleJob(func, delay):
    job_queue.run_once(func, delay)