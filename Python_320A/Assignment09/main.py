'''
Main driver for a simple social network project
'''
# pylint: disable=logging-fstring-interpolation
import csv
import os
import logging
import users
import user_status
import user_picture

USER_CSV_HEADER = ['USER_ID', 'NAME', 'LASTNAME', 'EMAIL']
STATUS_CSV_HEADER = ['STATUS_ID', 'USER_ID', 'STATUS_TEXT']

def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''
    return users.UserCollection()

def init_status_collection():
    '''
    Creates and returns a new instance of UserStatusCollection
    '''
    return user_status.UserStatusCollection()

def init_picture_collection():
    '''
    Creates and returns a new instance of UserStatusCollection
    '''
    return user_picture.PictureCollection()

def load_users(filename, user_collection):
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
    result = users.UserCollection.insert_many_users(user_collection, filename)
    return result

def load_status_updates(filename, status_collection):
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
    result = user_status.UserStatusCollection.insert_many_status(status_collection, filename)
    return result

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

def delete_user(user_id, status_collection, user_collection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    try:
        user_status.UserStatusCollection.delete_status_userid(status_collection, user_id)
    except KeyError:
        logging.info(f'No statues deleted for {user_id}.')
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

    if users.UserCollection.search_user(user_collection, user_id) is None:
        logging.info(f'add status failed, {user_id} user not found.')
        return False
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


def add_picture(user_id, tags, picture_collection, user_collection):
    '''
    Creates a new instance of picture tables.
    If there is no existing user_id the addition will be rejected.
    '''

    # cleans up the entry so that it matches format #string#string
    # list is also sorted
    hashtag = '#' + '#'.join(sorted(tags.split()))

    # Builds location path
    location = user_id + hashtag.replace('#','/')

    # foreign key check
    if users.UserCollection.search_user(user_collection, user_id) is None:
        logging.info(f'add picture failed, {user_id} user not found.')
        return False

    return user_picture.PictureCollection.\
            add_picture(picture_collection, user_id, hashtag, location)

def search_user_picture(user_id, picture_collection):
    '''
    search for all pictures associated with a user_id
    '''

    return user_picture.PictureCollection.\
        search_user_picture(picture_collection, user_id)

def search_directory(location, ext):
    '''
    Search any directory for a specific extention.
    '''
    subfolders, files = [], []

    for obj in os.scandir(location):
        if obj.is_dir():
            subfolders.append(obj.path)
        if obj.is_file():
            if os.path.splitext(obj.name)[1].lower() in ext:
                files.append(obj.path)

    for recur_location in list(subfolders):
        obj = search_directory(recur_location, ext)
        files.extend(obj)
    return files

def reconcile_images(picture_collection):
    '''
    Compares pictures in directory to pictures from dataset.
    Returns the differences and common list.
    '''
    db_list, disk_list = [], []

    db_pictures = user_picture.PictureCollection.\
        search_user_picture(picture_collection)

    for picture in db_pictures:
        db_list.append('temp/' + picture['LOCATION'] + '/' + picture['PICTURE_ID'])

    disk_list = search_directory('temp/', '.png')

    diff = set(db_list).symmetric_difference(set(disk_list))
    sim = set(db_list).intersection(set(disk_list))

    return sim, diff

def list_user_images(user_id):
    '''
    takes a user_id and search for all matching photos in temp/
    returns a tuple iterable
    '''
    results = []
    disk_list = search_directory('temp/', '.png')

    for item in disk_list:
        if 'temp/' + user_id + '/' in item:
            location_split = str(item).split('/')
            pic_id = location_split[-1]
            location = '/'.join(location_split[:-1])
            new = [user_id, location ,pic_id]
            results.append(new)

    return results
