'''
main driver for a simple social network project
'''
import csv
import users
import user_status

USER_CSV_HEADER = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
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
    with open(filename, encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=',')
        # check the header
        header = next(reader)
        if header != USER_CSV_HEADER:
            print("this doesn't look like an accounts file")
            return False
        new_users = []
        for row in reader:
            if row:  # skip completely empty rows
                # check for empty fields
                if '' in row:
                    return False
                try:
                    user_id, email, user_name, user_last_name = row
                except ValueError:
                    return False
                new_users.append((user_id, email, user_name, user_last_name))
        for user in new_users:
            user_collection.add_user(*user)

    # if it got this far, it all worked
    return True

def save_users(filename, user_collection):
    '''
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    '''
    try:
        with open(filename, 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(USER_CSV_HEADER)
            # note: not good to workdirectly with the internal dict
            #       but that's the only option -- prepare to refactor!
            #       but the tests should still be good :-)
            for user in user_collection.database.values():
                writer.writerow((user.user_id,
                                 user.email,
                                 user.user_name,
                                 user.user_last_name))
        return True
    except OSError:
        return False

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
    with open(filename, encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=',')
        # check the header
        header = next(reader)
        if header != STATUS_CSV_HEADER:
            print("this doesn't look like an status update file")
            return False
        new_users = []
        for row in reader:
            if row:  # skip completely empty rows
                # check for empty fields
                if '' in row:
                    return False
                try:
                    status_id, user_id, status_text = row
                except ValueError:
                    return False
                new_users.append((status_id, user_id, status_text))
        for user in new_users:
            status_collection.add_status(*user)

    # if it got this far, it all worked
    return True

def save_status_updates(filename, status_collection):
    '''
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    '''

    try:
        with open(filename, 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(STATUS_CSV_HEADER)
            # note: not good to workdirectly with the internal dict
            #       but that's the only option -- prepare to refactor!
            #       but the tests should still be good :-)
            for status in status_collection.database.values():
                writer.writerow((status.status_id,
                                 status.user_id,
                                 status.status_text))
        return True
    except OSError:
        return False

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
