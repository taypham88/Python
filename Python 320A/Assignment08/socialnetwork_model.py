'''Database model for social network'''

from pathlib import Path
from playhouse.dataset import DataSet

# pylint: disable=global-statement
HERE = Path(__file__).parent
PH_DB = []

def start_dataframe_db(filename = 'sqlite:///socialnetwork.db'):
    '''
    Initializes dataset db and sets it as a global
    '''

    global PH_DB
    PH_DB = DataSet(filename)
    return PH_DB

def initialize_userstable():
    '''
    Creates UsersTable in global db and sets user_id as unique
    '''

    users = PH_DB['UsersTable']

    # Create a dummy record to have a 'user_id' column
    users.insert(USER_ID='test')
    users.create_index(['USER_ID'], unique=True)
    # Delete the dummy record afterwards.
    users.delete(USER_ID='test')

    return users

def initialize_statustable():
    '''
    Creates UsersStatusTable in global db and sets status_id as unique
    '''

    user_status = PH_DB['UserStatusTable']

    # Create a dummy record to have a 'status_id' column
    user_status.insert(STATUS_ID='test')
    user_status.create_index(['STATUS_ID'], unique=True)
    # Delete the dummy record afterwards.
    user_status.delete(STATUS_ID='test')

    return user_status
