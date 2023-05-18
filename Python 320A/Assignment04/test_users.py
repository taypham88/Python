'''
Tests Main.py (users.py functions) the main driver code for Social Network
'''

import os
import unittest
from pathlib import Path
import main
import socialnetwork_model
import logging_setup_function
logging_setup_function.logging_setup()

HERE = Path(__file__).parent

def create_full_user_collection(database):
    """
    UserCollection, instead of drilling into other file's code to check the initial creation.
    it is best to create the user instances here. This was copied in the
    class solution.
    """
    users = [{'user_id': 'cbarker12',
              'email': 'cbarker@some_domain.com',
              'user_name': 'cbarker',
              'user_last_name': 'Barker',
              },
             {'user_id': 'fjones34',
              'email': 'jones@some_domain.com',
              'user_name': 'fjones',
              'user_last_name': 'Jones',
              },
             {'user_id': 'bwinkle678',
              'email': 'cwinkle@some_domain.com',
              'user_name': 'bwinkle',
              'user_last_name': 'Winkle',
              }]

    user_collection = main.init_user_collection(database)
    for user in users:
        user_collection.add_user(**user)
    return user_collection

def write_bad_header_users(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,LASTNAME,EMAIL
Brittaney.Gentry86,Brittaney.Gentry86@goodmail.com,Brittaney,Gentry
Keri.Royce8,Keri.Royce8@funmail.com,Keri,Royce
Michal.Hollyanne32,Michal.Hollyanne32@funmail.com,Michal,Hollyanne
Carolina.Mateusz51,Carolina.Mateusz51@goodmail.com,Carolina,Mateusz""")
    return filename

def write_bad_users(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
Brittaney.Gentry86,,Gentry,Gentry
Keri.Royce8,Keri.Royce8@funmail.com,Keri,Royce
Michal.Hollyanne32,Michal.Hollyanne32@funmail.com,Michal,Hollyanne
Carolina.Mateusz51,Carolina.Mateusz51@goodmail.com,Carolina,Mateusz""")
    return filename

def write_duplicate_users(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
Brittaney.Gentry86,Brittaney.Gentry86@goodmail.com,Gentry,Gentry
Keri.Royce8,Keri.Royce8@funmail.com,Keri,Royce
Michal.Hollyanne32,Michal.Hollyanne32@funmail.com,Michal,Hollyanne
Brittaney.Gentry86,Brittaney.Gentry86@goodmail.com,Gentry,Gentry""")
    return filename

def write_good_users(filename):
    """
    Creates a files for accounts.csv with bad extra data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
Channa.Formica62,Channa.Formica62@goodmail.com,Channa,Formica
Joanna.Publius21,Joanna.Publius21@goodmail.com,Joanna,Publius
Tonia.Saberio34,Tonia.Saberio34@goodmail.com,Tonia,Saberio
Lottie.Eustatius22,Lottie.Eustatius22@funmail.com,Lottie,Eustatius""")
    return filename

class TestUserCollection(unittest.TestCase):
    '''
    user.py UserCollection Testing
    '''

    def setUp(self):
        '''Setup for user_collection testing'''

        self.database = socialnetwork_model.start_database(':memory:')
        self.empty_user_collection = main.init_user_collection(self.database)
        self.full_user_collection = create_full_user_collection(self.database)

    @classmethod
    def setUpClass(cls):
        cls.bad_user_header_file = write_bad_header_users(HERE / "bad_user_header.csv")
        cls.bad_accounts_file = write_bad_users(HERE / "bad_users.csv")
        cls.good_users_file = write_good_users(HERE / "good_users.csv")
        cls.duplicate_users_file = write_duplicate_users(HERE / "duplicate_users.csv")

    @classmethod
    def tearDownClass(cls):
        os.remove(HERE / "bad_user_header.csv")
        os.remove(HERE / "bad_users.csv")
        os.remove(HERE / "good_users.csv")
        os.remove(HERE / "duplicate_users.csv")

    def test_search_user(self):
        '''
        search_user successful test
        '''

        user = main.search_user('fjones34',
                                self.full_user_collection)

        assert user.user_id == 'fjones34'
        assert user.email  == 'jones@some_domain.com'
        assert user.user_name == 'fjones'
        assert user.user_last_name == 'Jones'

    def test_search_user_fail(self):
        '''
        search_user unsuccessful test
        '''
        user = main.search_user('Penny100',
                                self.full_user_collection)

        assert user.user_id is None
        assert user.email is None
        assert user.user_name is None
        assert user.user_last_name is None

    def test_add_user(self):
        '''
        add_user successful test
        '''
        new_user = main.add_user('Tay100',
                                'tay@gmail.com',
                                'Tay',
                                'Pham',
                                self.full_user_collection)

        assert new_user is True
        assert main.search_user('Tay100', self.full_user_collection).user_id == 'Tay100'
        assert main.search_user('Tay100', self.full_user_collection).email == 'tay@gmail.com'
        assert main.search_user('Tay100', self.full_user_collection).user_name == 'Tay'
        assert main.search_user('Tay100', self.full_user_collection).user_last_name == 'Pham'

    def test_add_user_duplicate(self):
        '''
        add_user test for user already in collection
        '''
        new_user = main.add_user('cbarker12',
                               'this@something.com',
                               'fjones',
                               'Jones',
                               self.full_user_collection)

        assert new_user is False

    def test_update_user(self):
        '''
        update_user successful test
        '''

        mod_user = main.update_user\
            ('bwinkle678', 'updated@gmail.com', 'Dave', 'Y', self.full_user_collection)

        assert mod_user is True
        assert main.search_user('bwinkle678', \
            self.full_user_collection).user_id == 'bwinkle678'
        assert main.search_user('bwinkle678', \
            self.full_user_collection).email == 'updated@gmail.com'
        assert main.search_user('bwinkle678', \
            self.full_user_collection).user_name == 'Dave'
        assert main.search_user('bwinkle678', \
            self.full_user_collection).user_last_name == 'Y'

    def test_update_user_not_found(self):
        '''
        update_user unsuccessful test
        '''

        mod_user = main.update_user\
            ('Billy100', 'tay@gmail.com', 'Tay', 'Pham', self.full_user_collection)

        assert mod_user is False
        assert main.search_user('Billy100', \
            self.full_user_collection).user_id is None

    def test_delete_user(self):
        '''
        delete_user successful test
        '''

        delete_user = main.delete_user('bwinkle678', self.full_user_collection)

        assert delete_user is True
        assert main.search_user('bwinkle678', self.full_user_collection).user_id is None

    def test_delete_user_not_there(self):
        '''
        delete_user unsuccessful test
        '''
        delete_user = main.delete_user('Tay', self.full_user_collection)

        assert delete_user is False
        assert main.search_user('Tay', self.full_user_collection).user_id is None

    def test_load_users(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """
        result = main.load_users(self.good_users_file, self.database)

        assert result is True
        assert main.search_user('Channa.Formica62',\
            self.empty_user_collection).user_id == 'Channa.Formica62'
        assert main.search_user('Joanna.Publius21',\
            self.empty_user_collection).user_id == 'Joanna.Publius21'
        assert main.search_user('Tonia.Saberio34',\
            self.empty_user_collection).user_id == 'Tonia.Saberio34'
        assert main.search_user('Lottie.Eustatius22',\
            self.empty_user_collection).user_id == 'Lottie.Eustatius22'

    def test_load_users_bad(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_users(self.bad_accounts_file, self.database)

        assert result is False
        assert main.search_user('Brittaney.Gentry86', self.empty_user_collection).user_id is None
        assert main.search_user('Keri.Royce8', self.empty_user_collection).user_id is None
        assert main.search_user('Michal.Hollyanne32', self.empty_user_collection).user_id is None
        assert main.search_user('Carolina.Mateusz51', self.empty_user_collection).user_id is None

    def test_load_users_bad_header(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_users(self.bad_user_header_file, self.database)

        assert result is False
        assert main.search_user('Brittaney.Gentry86', self.empty_user_collection).user_id is None
        assert main.search_user('Keri.Royce8', self.empty_user_collection).user_id is None
        assert main.search_user('Michal.Hollyanne32', self.empty_user_collection).user_id is None
        assert main.search_user('Carolina.Mateusz51', self.empty_user_collection).user_id is None

    def test_load_users_no_file(self):
        """
        Tests when there is no file with the input name
        """

        result = main.load_users("badfile.csv", self.database)

        assert result is False

    def test_load_users_duplicate(self):
        """
        Tests when there is duplicate data in the csv when loading
        """
        result = main.load_users(self.duplicate_users_file, self.database)

        assert result is False

    def test_load_users_different_database(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """
        # Also provides coverage for clear = True

        database = socialnetwork_model.start_database('social.db', True)
        main_user_collection = main.init_user_collection(database)

        result = main.load_users(self.good_users_file, database)

        assert result is True
        assert main.search_user('Channa.Formica62',\
            main_user_collection).user_id == 'Channa.Formica62'
        assert main.search_user('Joanna.Publius21',\
            main_user_collection).user_id == 'Joanna.Publius21'
        assert main.search_user('Tonia.Saberio34',\
            main_user_collection).user_id == 'Tonia.Saberio34'
        assert main.search_user('Lottie.Eustatius22',\
            main_user_collection).user_id == 'Lottie.Eustatius22'

        os.remove(HERE / 'social.db')

    def test_load_users_noname_database(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """

        database = socialnetwork_model.start_database(None)
        main_user_collection = main.init_user_collection(database)

        result = main.load_users(self.good_users_file, database)

        assert result is True
        assert main.search_user('Channa.Formica62',\
            main_user_collection).user_id == 'Channa.Formica62'
        assert main.search_user('Joanna.Publius21',\
            main_user_collection).user_id == 'Joanna.Publius21'
        assert main.search_user('Tonia.Saberio34',\
            main_user_collection).user_id == 'Tonia.Saberio34'
        assert main.search_user('Lottie.Eustatius22',\
            main_user_collection).user_id == 'Lottie.Eustatius22'

        os.remove(HERE / 'social.db')
