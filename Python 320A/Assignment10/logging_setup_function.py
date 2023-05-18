'''
Function provides formating for logging used in this assignment.
'''
# pylint: disable=logging-fstring-interpolation, bare-except
import logging
from datetime import date
import functools
import sys

# Logging file's name format
format_date = date.today().strftime('%m_%d_%Y')

# logging code
def logging_setup():
    '''
    logging setup file used in users.py and user_status.py
    '''

    log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(f'log_{format_date}.log')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

def log_decorator(func):
    '''
    Logging decorator. Used for functions with exception handling.
    '''
    @functools.wraps(func)
    def log_decorator_wrapper(self, *args, **kwargs):
        try:
            value = func(self, *args, **kwargs)
        except:
            logging.error(f"Exception: {str(sys.exc_info()[1])} in {func}")
            return False
        return value
    return log_decorator_wrapper
