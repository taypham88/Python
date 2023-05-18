'''
classes to manage the user status messages
'''
# pylint: disable=R0903, R0201
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
            logging.info("Status not added, duplicate status found")
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
            logging.info("Status info not updated, user not found")
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
            logging.info("Status not deleted, status not found")
            return False

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        try:
            status = StatusTable.get(StatusTable.status_id == status_id)
        except pw.DoesNotExist:
            logging.info("search_status DoesNotExist, User not found")
            status = UserStatus(None, None, None)
        return status
