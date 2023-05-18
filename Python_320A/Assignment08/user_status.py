'''
classes to manage the user status messages
'''
# pylint: disable=logging-fstring-interpolation
import logging
import peewee as pw
import socialnetwork_model


class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self):
        self.statustable = socialnetwork_model.initialize_statustable()


    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        try:
            self.statustable.insert(STATUS_ID=status_id, USER_ID=user_id, STATUS_TEXT=status_text)
            return True
        except pw.IntegrityError:
            logging.info(f"Status {status_id} not added, duplicate status found")
            return False

    def insert_many_status(self, filename):
        '''
        Insert entire csv to database.
        '''
        try:
            self.statustable.thaw(format='csv', filename=filename)
        except pw.IntegrityError:
            logging.info(f"File {filename} has duplicate data")
            return False
        return True

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        result = self.statustable.update(STATUS_ID=status_id, \
            USER_ID=user_id, STATUS_TEXT=status_text, columns =['STATUS_ID'])
        return bool(result>0)

    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''

        result = self.statustable.delete(STATUS_ID=status_id)
        return bool(result>0)

    def delete_status_userid(self, user_id):
        '''
        deletes the status message with id, status_id
        '''

        result = self.statustable.delete(USER_ID=user_id)
        return bool(result>0)

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''

        status = self.statustable.find_one(STATUS_ID = status_id)
        if status is None:
            logging.info(f"search_status DoesNotExist, User {status_id} not found")
        return status
