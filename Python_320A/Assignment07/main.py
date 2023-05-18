'''
main driver for a simple social network project
'''
# pylint: disable=logging-fstring-interpolation, consider-using-with

import csv
import logging
import multiprocessing
from pymongo import MongoClient
import pandas as pd

import users
import user_status

USER_CSV_HEADER = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
STATUS_CSV_HEADER = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']

def customize_user(generator):
    'renames users headers to table names'

    for row in generator:
        row['_id'] = row['USER_ID']
        del row['USER_ID']
        row['user_name'] = row['NAME']
        del row['NAME']
        row['user_last_name'] = row['LASTNAME']
        del row['LASTNAME']
        row['email'] = row['EMAIL']
        del row['EMAIL']
        yield row

def customize_status(generator):
    'renames status headers to table names'

    for row in generator:
        row['_id'] = row['STATUS_ID']
        del row['STATUS_ID']
        row['user_id'] = row['USER_ID']
        del row['USER_ID']
        row['status_text'] = row['STATUS_TEXT']
        del row['STATUS_TEXT']
        yield row

def start_mongo():
    """
    start up a connection to MongoDB
    :returns: A pymongo client object, and a database object
    """

    # In production code, these would be read from a config file, or ...
    # these values should match what's in mongo_config_dev.yml
    client = MongoClient(host='127.0.0.1', port=27017)

    return client

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

def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    return users.UserCollection.search_user(user_collection, user_id)

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
    return users.UserCollection.\
        modify_user(user_collection, user_id, email, user_name, user_last_name)

def delete_user(user_id, user_collection, status_collection):
    '''
    Deletes a user from user_collection, removes all status with user_id associated with it.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    user_status.UserStatusCollection.delete_all(status_collection, user_id)
    return users.UserCollection.delete_user(user_collection, user_id)

def add_status(user_id, status_id, status_text, status_collection, user_collection):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    if users.UserCollection.search_user(user_collection, user_id).user_id is None:
        logging.info(f"{status_id} not added, user {user_id} doesn't exist.")
        return False
    return user_status.UserStatusCollection.\
        add_status(status_collection, status_id, user_id, status_text)

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

def update_status(status_id, user_id, status_text, status_collection, user_collection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    if users.UserCollection.search_user(user_collection, user_id).user_id is None:
        logging.info(f"{status_id} not added, user {user_id} doesn't exist.")
        return False
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

def load_users(filename, user_collection, size = 500):
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
    try:
        with open(filename, encoding='utf-8') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            header = next(reader)
            if header != USER_CSV_HEADER: # check the header
                logging.warning(f"{filename} did not load, headers errors detected.")
                return False
            for row in reader:
                if row:  # skip completely empty rows
                    # check for empty fields
                    if '' in row:
                        logging.warning(f"{filename} didn't load, data missing.")
                        return False
    except FileNotFoundError:
        logging.info(f"No file matching {filename}, no UsersTable has been created.")
        return False
    all_proc =[]
    for chunk in pd.read_csv(filename, chunksize=size, iterator=True):
        proc = multiprocessing.Process(target = insert_manyusers_multi(chunk, user_collection))
        all_proc.append(proc)
        proc.start()
    for proc in all_proc:
        proc.join()
    return True


def insert_manyusers_multi(chunk, user_collection):
    '''Converts to a dictionary and accesses insert many for users.'''

    p_chunk = customize_user(chunk.to_dict('records'))
    users.UserCollection.insert_many_users(user_collection, p_chunk)


def load_status_updates(filename, status_collection, user_collection, size = 50000):
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
    try:
        with open(filename, encoding='utf-8') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            header = next(reader)
            if header != STATUS_CSV_HEADER:
                logging.warning(f"{filename} did not load, headers errors detected.")
                return False
            for row in reader:
                if row:
                    if '' in row:
                        logging.warning(f"{filename} didn't load, data missing.")
                        return False
    except FileNotFoundError:
        logging.info(f"No file matching {filename}, no StatusTable has been created.")
        return False
    all_proc =[]
    for chunk in pd.read_csv(filename, chunksize=size, iterator=True):
        proc = multiprocessing.Process\
            (target = insert_manystatus_multi(chunk, status_collection, user_collection))
        all_proc.append(proc)
        proc.start()
    for proc in all_proc:
        proc.join()
    return True

def insert_manystatus_multi(chunk, status_collection, user_collection):
    '''Accesses insert many for status and converts it to dictionary.
    Also performs user_id check.'''

    p_chunk = customize_status(chunk.to_dict('records'))
    s_status =[]
    for row in p_chunk:
        if users.UserCollection.search_user(user_collection, row['user_id']).user_id is not None:
            s_status.append(row)
    user_status.UserStatusCollection.insert_many_status(status_collection, s_status)
