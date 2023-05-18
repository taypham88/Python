'''
Tests Main.py (users.py functions) the main driver code for Social Network
'''
# pylint: disable=too-many-public-methods
import os
import unittest
from pathlib import Path
import main
import socialnetwork_model
import logging_setup_function
logging_setup_function.logging_setup()

HERE = Path(__file__).parent

def create_full_user_collection():
    """
    UserCollection, instead of drilling into other file's code to check the initial creation.
    it is best to create the user instances here. This was copied in the
    class solution.
    """
    users = [{'USER_ID': 'cbarker12',
              'EMAIL': 'cbarker@some_domain.com',
              'NAME': 'cbarker',
              'LASTNAME': 'Barker'
              },
             {'USER_ID': 'fjones34',
              'EMAIL': 'jones@some_domain.com',
              'NAME': 'fjones',
              'LASTNAME': 'Jones'
              },
             {'USER_ID': 'bwinkle678',
              'EMAIL': 'cwinkle@some_domain.com',
              'NAME' : 'bwinkle',
              'LASTNAME': 'Winkle'}]

    user_collection = main.init_user_collection()
    for user in users:
        main.add_user(user['USER_ID'], user['EMAIL'],\
            user['NAME'], user['LASTNAME'],user_collection)
    return user_collection

def write_bad_header_users(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,LASTNAME,EMAIL
Brittaney.Gentry86,Brittaney,Gentry,Brittaney.Gentry86@goodmail.com
Keri.Royce8,Keri,Royce,Keri.Royce8@funmail.com
Michal.Hollyanne32,Michal,Hollyanne,Michal.Hollyanne32@funmail.com
Carolina.Mateusz51,Carolina,Mateusz,Carolina.Mateusz51@goodmail.comn""")
    return filename

def write_bad_users(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,NAME,LASTNAME,EMAIL
Brittaney.Gentry86,,Gentry,Brittaney.Gentry86@goodmail.com
Keri.Royce8,Keri,Royce,Keri.Royce8@funmail.com
Michal.Hollyanne32,Michal,Hollyanne,Michal.Hollyanne32@funmail.com
Carolina.Mateusz51,Carolina,Mateusz,Carolina.Mateusz51@goodmail.com""")
    return filename

def write_duplicate_users(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,NAME,LASTNAME,EMAIL
Brittaney.Gentry86,Gentry,Gentry,Brittaney.Gentry86@goodmail.com
Keri.Royce8,Keri,Royce,Keri.Royce8@funmail.com
Michal.Hollyanne32,Michal,Hollyanne,Michal.Hollyanne32@funmail.com
Brittaney.Gentry86,Gentry,Gentry,Brittaney.Gentry86@goodmail.com""")
    return filename

def write_good_users(filename):
    """
    Creates a files for accounts.csv with bad extra data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,NAME,LASTNAME,EMAIL
Channa.Formica62,Channa,Formica,Channa.Formica62@goodmail.com
Joanna.Publius21,Joanna,Publius,Joanna.Publius21@goodmail.com
Tonia.Saberio34,Tonia,Saberio,Tonia.Saberio34@goodmail.com
Lottie.Eustatius22,Lottie,Eustatius,Lottie.Eustatius22@funmail.com""")
    return filename


class TestUserCollection(unittest.TestCase):
    '''
    user.py UserCollection Testing
    '''

    def setUp(self):
        '''Setup for user_collection testing'''

        with socialnetwork_model.start_dataframe_db('sqlite:///:memory:'):
            self.empty_user_collection = main.init_user_collection()
            self.empty_status_collection = main.init_status_collection()
            self.full_user_collection = create_full_user_collection()

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

        assert user['USER_ID'] == 'fjones34'
        assert user['EMAIL']   == 'jones@some_domain.com'
        assert user['NAME']  == 'fjones'
        assert user['LASTNAME']  == 'Jones'

    def test_search_user_fail(self):
        '''
        search_user unsuccessful test
        '''
        user = main.search_user('Penny100',
                                self.full_user_collection)

        assert user is None

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
        assert main.search_user('Tay100', self.full_user_collection)['USER_ID'] == 'Tay100'
        assert main.search_user('Tay100', self.full_user_collection)['EMAIL'] == 'tay@gmail.com'
        assert main.search_user('Tay100', self.full_user_collection)['NAME'] == 'Tay'
        assert main.search_user('Tay100', self.full_user_collection)['LASTNAME'] == 'Pham'

    def test_add_userid_char_fail(self):
        '''
        add_user fails due to user id being longer than 30 characters
        '''
        user_id = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        new_user = main.add_user(user_id,
                                'tay@gmail.com',
                                'Tay',
                                'Pham',
                                self.full_user_collection)

        assert new_user is False

    def test_add_username_char_fail(self):
        '''
        add_user fails due to user first name being longer than 30 characters
        '''
        user_name = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        new_user = main.add_user('Tay100',
                                'tay@gmail.com',
                                user_name,
                                'Pham',
                                self.full_user_collection)

        assert new_user is False

    def test_add_userlastname_char_fail(self):
        '''
        add_user fails due to last name being longer than 100 characters
        '''
        user_lastname = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
                AAAAAAAAAAAAAAAAA'
        new_user = main.add_user('Tay100',
                                'tay@gmail.com',
                                'Tay',
                                user_lastname,
                                self.full_user_collection)

        assert new_user is False

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
            self.full_user_collection)['USER_ID'] == 'bwinkle678'
        assert main.search_user('bwinkle678', \
            self.full_user_collection)['EMAIL'] == 'updated@gmail.com'
        assert main.search_user('bwinkle678', \
            self.full_user_collection)['NAME'] == 'Dave'
        assert main.search_user('bwinkle678', \
            self.full_user_collection)['LASTNAME']  == 'Y'

    def test_update_user_name_char_fail(self):
        '''
        update_user fails to update because user id is more than 30 characters
        '''
        name = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

        mod_user = main.update_user\
            ('bwinkle678', 'updated@gmail.com', name, 'Y', self.full_user_collection)

        assert mod_user is False

    def test_update_user_lastname_char_fail(self):
        '''
        update_user fails to update because user id is more than 30 characters
        '''
        last = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

        mod_user = main.update_user\
            ('bwinkle678', 'updated@gmail.com', 'Dave', last, self.full_user_collection)

        assert mod_user is False

    def test_update_user_not_found(self):
        '''
        update_user unsuccessful test
        '''

        mod_user = main.update_user\
            ('Billy100', 'tay@gmail.com', 'Tay', 'Pham', self.full_user_collection)

        assert mod_user is False
        assert main.search_user('Billy100', \
            self.full_user_collection) is None

    def test_delete_user(self):
        '''
        delete_user successful test
        '''

        delete_user = main.delete_user('bwinkle678', \
            self.empty_status_collection, self.full_user_collection)

        assert delete_user is True
        assert main.search_user('bwinkle678', self.full_user_collection) is None

    def test_delete_user_not_there(self):
        '''
        delete_user unsuccessful test
        '''
        delete_user = main.delete_user('Tay', \
            self.empty_status_collection, self.full_user_collection)

        assert delete_user is False
        assert main.search_user('Tay', self.full_user_collection) is None

    def test_load_users(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """
        result = main.load_users(self.good_users_file, self.empty_user_collection)

        assert result is True
        assert main.search_user('Channa.Formica62',\
            self.empty_user_collection)['USER_ID'] == 'Channa.Formica62'
        assert main.search_user('Joanna.Publius21',\
            self.empty_user_collection)['USER_ID'] == 'Joanna.Publius21'
        assert main.search_user('Tonia.Saberio34',\
            self.empty_user_collection)['USER_ID'] == 'Tonia.Saberio34'
        assert main.search_user('Lottie.Eustatius22',\
            self.empty_user_collection)['USER_ID'] == 'Lottie.Eustatius22'

    def test_load_users_bad(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_users(self.bad_accounts_file, self.empty_user_collection)

        assert result is False
        assert main.search_user('Brittaney.Gentry86', self.empty_user_collection) is None
        assert main.search_user('Keri.Royce8', self.empty_user_collection) is None
        assert main.search_user('Michal.Hollyanne32', self.empty_user_collection) is None
        assert main.search_user('Carolina.Mateusz51', self.empty_user_collection) is None

    def test_load_users_bad_header(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_users(self.bad_user_header_file, self.empty_user_collection)

        assert result is False
        assert main.search_user('Brittaney.Gentry86', self.empty_user_collection) is None
        assert main.search_user('Keri.Royce8', self.empty_user_collection) is None
        assert main.search_user('Michal.Hollyanne32', self.empty_user_collection) is None
        assert main.search_user('Carolina.Mateusz51', self.empty_user_collection) is None

    def test_load_users_no_file(self):
        """
        Tests when there is no file with the input name
        """

        result = main.load_users("badfile.csv", self.empty_user_collection)

        assert result is False

    def test_load_users_duplicate(self):
        """
        Tests when there is duplicate data in the csv when loading
        """
        result = main.load_users(self.duplicate_users_file, self.empty_user_collection)

        assert result is False
