'''
Classes for user information for the social network project
'''
# pylint: disable=logging-fstring-interpolation
import logging
import peewee as pw
from cerberus import Validator
import socialnetwork_model


char30 = Validator({'characterlength': {'min': 0, 'max': 30}})
char100 = Validator({'characterlength': {'min': 0, 'max': 100}})

class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self):

        self.usertable = socialnetwork_model.initialize_userstable()


    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        if char30.validate({'characterlength' : len(user_id)}) is False:
            logging.info(f"User id {user_id} is more than 30 characters")
            return False

        if char30.validate({'characterlength' : len(user_name)}) is False:
            logging.info(f"User name {user_name} is more than 30 characters")
            return False

        if char100.validate({'characterlength' : len(user_last_name)}) is False:
            logging.info(f"User last name {user_last_name} is more than 100 characters")
            return False

        try:
            self.usertable.insert(USER_ID=user_id, \
                NAME=user_name, LASTNAME=user_last_name, EMAIL=email)
            return True
        except pw.IntegrityError:
            logging.info(f"User {user_id} not added, duplicate user found")
            return False

    def insert_many_users(self, filename):
        '''
        Inserts entire csv into database
        '''
        try:
            self.usertable.thaw(format='csv', filename=filename)
        except pw.IntegrityError:
            logging.info(f"File {filename} has duplicate data")
            return False
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''

        if char30.validate({'characterlength' : len(user_name)}) is False:
            logging.info(f"User name {user_name} is more than 30 characters")
            return False

        if char30.validate({'characterlength' : len(user_last_name)}) is False:
            logging.info(f"User last name {user_last_name} is more than 100 characters")
            return False

        result = self.usertable.update(USER_ID=user_id, \
            NAME=user_name, LASTNAME=user_last_name, EMAIL=email, columns =['USER_ID'])
        return bool(result>0)

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''

        result = self.usertable.delete(USER_ID=user_id)
        return bool(result>0)


    def search_user(self, user_id):
        '''
        Searches for user data
        '''

        user = self.usertable.find_one(USER_ID = user_id)
        if user is None:
            logging.info(f"search_user DoesNotExist, User {user_id} not found")
        return user
