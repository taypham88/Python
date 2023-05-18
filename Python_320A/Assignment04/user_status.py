'''
classes to manage the user status messages
'''
# pylint: disable=R0903, R0201, W1203
import logging
import peewee as pw
from socialnetwork_model import StatusTable


class UserStatus():
    '''
    class to hold status message data
    '''

    def __init__(self, status_id, user_id, status_text):
        self.status_id = status_id
        self.user_id = user_id
        self.status_text = status_text


class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self,database):
        self.database = database


    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        try:
            new_status = StatusTable.create(status_id = status_id,
                                            user_id = user_id, status_text = status_text)
            new_status.save()
            return True
        except pw.IntegrityError:
            logging.info(f"Status not added, duplicate status {status_id} found")
            return False

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        try:
            status = StatusTable.get(StatusTable.status_id == status_id)
            if status.status_id == status_id:
                status.user_id = user_id
                status.status_text = status_text
                status.save()
            return True
        except pw.DoesNotExist:
            logging.info(f"Status info not updated, Status {status_id} not found")
            return False

    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        try:
            status = StatusTable.get(StatusTable.status_id == status_id)
            if status.status_id == status_id:
                status.delete_instance()
            return True
        except pw.DoesNotExist:
            logging.info(f"Status not deleted, status {status_id} not found")
            return False

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        try:
            status = StatusTable.get(StatusTable.status_id == status_id)
        except pw.DoesNotExist:
            logging.info(f"search_status DoesNotExist, Status {status_id} not found")
            status = UserStatus(None, None, None)
        return status

    def search_all_status_updates(self, user_id):
        '''Takes input user_id and returns all statuses
        for that user in a list of tuples.
        '''
        query = StatusTable.select().where(StatusTable.user_id == user_id).iterator()
        status_collected = []
        try:
            while True:
                next_status = next(query)
                match_status = (next_status.status_text)
                status_collected.append(match_status)
        except StopIteration:
            logging.info(f"Search Status has completed \
iteration with {len(status_collected)} results.")
            return status_collected

    def filter_status_by_string(self, filter_string :str):
        '''Searches for all status text that contains input string.'''

        return StatusTable.select().where(StatusTable.status_text.contains\
            (filter_string)).iterator()
