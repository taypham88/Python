'''
Function provides formating for logging used in this assignment.
'''
import logging
from datetime import date

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
