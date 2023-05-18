'''
classes to manage the user status messages
'''
# pylint: disable=logging-fstring-interpolation

import logging
from dataclasses import dataclass
from pymongo.errors import DuplicateKeyError

@dataclass
class UserStatus:
    '''
    class to hold status message data
    '''

    status_id: str
    user_id: str
    status_text: str

class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self, mongodb):
        """initialize a UserCollection"""
        self.mongodb = mongodb  # just in case we need it
        self.status_col = mongodb.status

    def __len__(self):
        """ number of status in the collection """
        return self.status_col.count_documents({})

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id
        '''
        status = self.status_col.find_one({'_id': status_id})
        if status is None:
            logging.info(f"search_status for {status_id}, returned None.")
            return UserStatus(None, None, None)
        return UserStatus(status['_id'], status['user_id'], status['status_text'])

    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        new_status = {'_id': status_id, 'user_id': user_id, \
            'status_text': status_text}
        try:
            self.status_col.insert_one(new_status)

        except DuplicateKeyError:
            logging.warning(f"add_status failed for\
{status_id}, duplicate status found.")
            return False
        return True

    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''

        if self.status_col.find_one({'_id': status_id}) is None:
            logging.info(f"delete_status failed for {status_id}, no status found.")
            return False
        self.status_col.delete_one({'_id': status_id})
        return True

    def delete_all(self, user_id):
        '''deletes all instances of user_id in status collection'''

        search_id = self.status_col.find_one({'user_id': user_id})
        if search_id is not None:
            self.status_col.delete_many({'user_id': user_id})
            logging.info(f"delete_all for {user_id} was called.")
            return True
        return False

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''

        db_filter = {'_id': status_id}
        new_values = {'$set': {'user_id': user_id, \
            'status_text': status_text}}

        if self.status_col.find_one({'_id': status_id}) is None:
            logging.info(f"Modify_user failed for {status_id}, no status found.")
            return False
        self.status_col.update_one(db_filter, new_values)
        return True

    def insert_many_status(self, status_dict):
        '''
        add a new status message to the collection
        '''
        if len(status_dict) > 0:
            self.status_col.insert_many(status_dict)
            return True
        return False
