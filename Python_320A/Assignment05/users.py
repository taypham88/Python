'''
Classes for user information for the social network project
'''
# pylint: disable=logging-fstring-interpolation
import logging
from dataclasses import dataclass
from pymongo.errors import DuplicateKeyError


@dataclass
class Users:
    '''
    Contains user information
    '''
    user_id: str
    user_name: str
    user_last_name: str
    email: str

class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self, mongodb):
        """initialize a UserCollection"""
        self.mongodb = mongodb  # just in case we need it
        self.user_col = mongodb.users

    def __len__(self):
        """ number of users in the collection """
        return self.user_col.count_documents({})

    def search_user(self, user_id):
        '''
        Searches for user in collection
        '''

        user = self.user_col.find_one({'_id': user_id})
        if user is None:
            logging.info(f"search_user for {user_id}, returned None.")
            return Users(None, None, None, None)
        return Users(user['_id'], user['user_name'], user['user_last_name'], user['email'])

    def add_user(self, user_id, user_name, user_last_name, email):
        '''
        Adds a new user to the collection
        '''
        new_user = {'_id': user_id, 'user_name': user_name, \
            'user_last_name': user_last_name, 'email': email}

        try:
            self.user_col.insert_one(new_user)

        except DuplicateKeyError:
            logging.warning(f"add_user failed for {user_id}, duplicate user found.")
            return False
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        db_filter = {'_id': user_id}
        new_values = {'$set': {'user_name': user_name, \
            'user_last_name': user_last_name, 'email': email}}

        if self.user_col.find_one(db_filter) is None:
            logging.info(f"Modify_user failed for {user_id}, no user found.")
            return False
        self.user_col.update_one(db_filter, new_values)
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''

        if self.user_col.find_one({'_id': user_id}) is None:
            logging.info(f"delete_user failed for {user_id}, no user found.")
            return False
        self.user_col.delete_one({'_id': user_id})
        return True

    def insert_many_users(self, dict_list):
        '''Allows for insert many'''

        self.user_col.insert_many(dict_list)
        return True
