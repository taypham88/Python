'''
Classes for user information for the social network project
'''
# pylint: disable=R0903, R0201
import logging
import peewee as pw
from socialnetwork_model import UsersTable


class Users():
    '''
    Contains user information
    '''

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name

class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self, database):

        self.database = database


    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        try:
            new_user = UsersTable.create(user_id = user_id, user_name = user_name,
                                            user_last_name = user_last_name, email = email)
            new_user.save()
            return True
        except pw.IntegrityError:
            logging.info("User not added, duplicate user found")
            return False

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        try:
            user = UsersTable.get(UsersTable.user_id == user_id)
            if user.user_id == user_id:
                user.email = email
                user.user_name = user_name
                user.user_last_name = user_last_name
                user.save()
            return True
        except pw.DoesNotExist:
            logging.info("User info not updated, user not found")
            return False

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        try:
            user = UsersTable.get(UsersTable.user_id == user_id)
            if user.user_id == user_id:
                user.delete_instance()
            return True
        except pw.DoesNotExist:
            logging.info("User info not deleted, user not found")
            return False

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        try:
            user = UsersTable.get(UsersTable.user_id == user_id)
        except pw.DoesNotExist:
            logging.info("search_user DoesNotExist, User not found")
            user = Users(None, None, None, None)
        return user
