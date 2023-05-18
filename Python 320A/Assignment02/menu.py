'''
Provides a basic frontend
'''

import sys
import main


def load_users(user_collection):
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)


def load_status_updates(status_collection):
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename, status_collection)


def add_user(user_collection):
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection):
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
    if not main.update_user(user_id, email, user_name, user_last_name, user_collection):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")


def search_user(user_collection):
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
    if not result.user_id:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")


def delete_user(user_collection):
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def save_users(user_collection):
    '''
    Saves user database into a file
    '''
    filename = input('Enter filename for users file: ')
    main.save_users(filename, user_collection)


def add_status(status_collection):
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(user_id, status_id, status_text, status_collection):
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
    if not main.add_status(user_id, status_id, status_text, status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status(status_collection):
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if not result.status_id:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Status ID: {result.status_id}")
        print(f"Status text: {result.status_text}")


def delete_status(status_collection):
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def save_status(status_collection):
    '''
    Saves status database into a file
    '''
    filename = input('Enter filename for status file: ')
    main.save_status_updates(filename, status_collection)


def quit_program():
    '''
    Quits program
    '''
    sys.exit()

def menu_options_function():
    '''function that allows for user selected menu options'''

    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': save_users,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'L': save_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Save user database to file
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            L: Save status database to file
                            Q: Quit

                            Please enter your choice: """).upper()
        if user_selection in menu_options:

            if user_selection in ('A', 'C', 'D', 'E', 'F', 'G'):
                menu_options[user_selection](main_user_collection)

            elif user_selection in ('Q'):
                menu_options[user_selection]()

            else:
                menu_options[user_selection](main_status_collection)

        else:
            print("Invalid option")

def initialize():
    '''initializes user and status collections'''

    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()

    return user_collection, status_collection


if __name__ == '__main__':
    main_user_collection, main_status_collection = initialize()
    menu_options_function()
