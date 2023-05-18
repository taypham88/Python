'''
Classes for user information for the social network project
'''
# pylint: disable=R0903
import logging
import logging_setup_function

# Logging function setup call
logging_setup_function.logging_setup()

class Users():
    '''
    Contains user information
    '''

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name
        logging.info("User Class function called.")


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self):
        self.database = {}

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        if user_id in self.database:
            # Rejects new status if status_id already exists
            logging.warning("users.add_user returned False, no user_id found.")
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        if user_id not in self.database:
            logging.warning("users.modify_user returned False, no user_id found.")
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        if user_id not in self.database:
            logging.warning("users.delete_user returned False, no user_id found.")
            return False
        del self.database[user_id]
        return True

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        if user_id not in self.database:
            logging.warning("users.search_user returned Users(None...), no user_id found.")
            return Users(None, None, None, None)
        return self.database[user_id]
