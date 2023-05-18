'''
Provides a basic frontend
'''
#pylint: disable=R1719
import os
from pathlib import Path
import sys
import main
import socialnetwork_model
import logging_setup_function as log

HERE = Path(__file__).parent

def load_users(user_collection):
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')

    if os.path.isfile(HERE / filename) is False:
        print('File not in directory')
    else:
        main.load_users(filename, user_collection)
        print('User data uploaded')


def load_status_updates(status_collection):
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    if os.path.isfile(HERE / filename) is False:
        print('File not in directory')
    else:
        main.load_status_updates(filename, status_collection)
        print('UserStatus data uploaded')


def add_user(user_collection):
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection) is False:
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user(user_collection):
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if main.update_user(user_id, email, user_name, user_last_name, user_collection) is False:
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")


def search_user(user_collection):
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
    if result is None:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Email: {result['EMAIL']}")
        print(f"Name: {result['NAME']}")
        print(f"Last name: {result['LASTNAME']}")


def delete_user(status_collection, user_collection):
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if main.delete_user(user_id, status_collection,user_collection) is False:
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def add_status(status_collection, user_collection):
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if main.add_status(user_id, status_id, \
        status_text, status_collection, user_collection) is False:
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status(status_collection):
    '''
    Updates information for an existing status
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if main.update_status(status_id, user_id, \
        status_text, status_collection) is False:
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status(status_collection):
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if result is None:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Status ID: {result['STATUS_ID']}")
        print(f"Status text: {result['STATUS_TEXT']}")


def delete_status(status_collection):
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if main.delete_status(status_id, status_collection) is False:
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def quit_program():
    '''
    Quits program
    '''
    if os.path.isfile(HERE /'socialnetwork.db') is True:
        os.remove(HERE/'socialnetwork.db')
    sys.exit()

def menu_options_function(user_collection, status_collection):
    '''function that allows for user selected menu options'''

    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': add_status,
        'H': update_status,
        'I': search_status,
        'J': delete_status,
        'K': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Add status
                            H: Update status
                            I: Search status
                            J: Delete status
                            K: Quit

                            Please enter your choice: """).upper()
        if user_selection in menu_options:

            if user_selection in ('C', 'D', 'E', 'A'):
                menu_options[user_selection](user_collection)

            elif user_selection in ('G', 'F'):
                menu_options[user_selection](status_collection,user_collection)

            elif user_selection in ('K'):
                menu_options[user_selection]()

            else:
                menu_options[user_selection](status_collection)

        else:
            print("Invalid option")

def initialize():
    '''initializes user and status collections'''

    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()

    return user_collection, status_collection


if __name__ == '__main__':

    log.logging_setup()
    if os.path.isfile(HERE /'socialnetwork.db') is True:
        os.remove(HERE/'socialnetwork.db')
    database = socialnetwork_model.start_dataframe_db()
    main_user_collection, main_status_collection = initialize()
    menu_options_function(main_user_collection, main_status_collection)
