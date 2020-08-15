import atexit
from time import time, strftime, localtime
from datetime import timedelta

"""
HelloWorld
"""


def secondsToStr(elapsed=None):
    '''
    Tnis is secondsToStr Function
    '''
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%m:%S", localtime())

    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    """
    This is log function
    """

    line = "=" * 40
    print(line)
    print(f"{secondsToStr()}-{s}")

    if elapsed:
        print(f"Elapsed time : {elapesed}")

    print(line)
    # return


def endlog():
    '''
    endlog
    '''
    end = time()
    elapsed = end - start
    log("End Program", secondsToStr(elapsed))


start = localtime()
atexit.register(endlog)
log("Start Program")
