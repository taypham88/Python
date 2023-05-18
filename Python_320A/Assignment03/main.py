'''
Main driver for a simple social network project
'''
# pylint: disable=R1732
import csv
import logging
import peewee as pw
import users
import user_status
from socialnetwork_model import UsersTable, StatusTable

USER_CSV_HEADER = ['USER_ID', 'NAME', 'LASTNAME', 'EMAIL']
STATUS_CSV_HEADER = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']

def init_user_collection(database):
    '''
    Creates and returns a new instance of UserCollection
    '''
    return users.UserCollection(database)

def init_status_collection(database):
    '''
    Creates and returns a new instance of UserStatusCollection
    '''
    return user_status.UserStatusCollection(database)

def load_users(filename, database):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''

    # checks the csv header and data before trying to build database
    try:
        with open(filename, encoding='utf-8') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            header = next(reader)
            if header != USER_CSV_HEADER: # check the header
                logging.info("Users csv file doesn't look like an accounts file")
                return False
            for row in reader:
                if row:  # skip completely empty rows
                    # check for empty fields
                    if '' in row:
                        logging.info('Users csv file has blank data')
                        return False
    except FileNotFoundError:
        logging.info('No file matching entered value, no UsersTable has been created.')
        return False
    try:
        dict_reader = csv.DictReader(open(filename, encoding='utf-8'))
        with database.atomic():
            for row in dict_reader :
                UsersTable.create(user_id = row['USER_ID'], user_name = row['NAME'],
                                    user_last_name = row['LASTNAME'], email = row['EMAIL'])
    except pw.IntegrityError:
        logging.info("UsersTable not created, duplicate user found")
        return False
    return True

def load_status_updates(filename, database):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    '''
    # checks the csv header and data before trying to build database
    try:
        with open(filename, encoding='utf-8') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            header = next(reader)
            if header != STATUS_CSV_HEADER: # check the header
                logging.info("Status csv file doesn't look like an accounts file")
                return False
            for row in reader:
                if row:  # skip completely empty rows
                    # check for empty fields
                    if '' in row:
                        logging.info('Status csv file has blank data')
                        return False
    except FileNotFoundError:
        logging.info('No file matching entered value, no StatusTable has been created.')
        return False
    try:
        dict_reader = csv.DictReader(open(filename, encoding='utf-8'))
        with database.atomic():
            for row in dict_reader :
                StatusTable.create(status_id = row['STATUS_ID'], user_id = row['USER_ID'],
                                    status_text= row['STATUS_TEXT'])
    except pw.IntegrityError:
        logging.info("StatusTable not created, duplicate user found")
        return False
    return True

def add_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    return users.UserCollection.\
        add_user(user_collection, user_id, email, user_name, user_last_name)

def update_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return users.UserCollection.modify_user\
        (user_collection, user_id, email, user_name, user_last_name)

def delete_user(user_id, user_collection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    return users.UserCollection.delete_user(user_collection, user_id)

def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    return users.UserCollection.search_user(user_collection, user_id)

def add_status(user_id, status_id, status_text, status_collection):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    return user_status.UserStatusCollection.\
        add_status(status_collection, status_id, user_id, status_text)

def update_status(status_id, user_id, status_text, status_collection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return user_status.UserStatusCollection.\
        modify_status(status_collection, status_id, user_id, status_text)

def delete_status(status_id, status_collection):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    return user_status.UserStatusCollection.\
        delete_status(status_collection, status_id)


def search_status(status_id, status_collection):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    return user_status.UserStatusCollection.\
        search_status(status_collection, status_id)
