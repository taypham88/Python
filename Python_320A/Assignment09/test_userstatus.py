'''
Tests Main.py (user_status.py functions) the main driver code for Social Network
'''

import os
import unittest
from pathlib import Path
import socialnetwork_model
import main
import test_users
import logging_setup_function
logging_setup_function.logging_setup()

HERE = Path(__file__).parent

def create_full_status_collection(user_collection):
    """
    UserStatusCollection, instead of drilling into other file's code to check the initial creation.
    it is best to create the user instances here. This was copied in the
    class solution.
    """
    status = [{'STATUS_ID': 'cbarker12_00001',
              'USER_ID': 'cbarker12',
              'STATUS_TEXT': "Code is finally compiling",
              },
             {'STATUS_ID': 'fjones34_00001',
              'USER_ID': 'fjones34',
              'STATUS_TEXT': "Sunny in Seattle this morning",
              },
             {'STATUS_ID': 'bwinkle678_00002',
              'USER_ID': 'bwinkle678',
              'STATUS_TEXT': "Perfect weather for a hike",
              },
             {'STATUS_ID': 'bwinkle678_00003',
              'USER_ID': 'bwinkle678',
              'STATUS_TEXT': "A different status",
              }]

    status_collection = main.init_status_collection()
    for item in status:
        main.add_status(item['USER_ID'],item['STATUS_ID'],\
            item['STATUS_TEXT'], status_collection, user_collection)
    return status_collection

def write_bad_header_status(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,,STATUS_TEXT
Channa.Formica62_01,Channa.Formica62,thinkable existence hug aback sky
Joanna.Publius21_01,Joanna.Publius21,cooing fireman withstand grotesque year
Tonia.Saberio34_01,Tonia.Saberio34,juvenile toothpaste fix odd breakfast
Lottie,Eustatius_01,Lottie,Eustatius,Lottie.Eustatius22@funmail.com""")
    return filename

def write_bad_status(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
Channa.Formica62_01,,thinkable existence hug aback sky
Joanna.Publius21_01,Joanna.Publius21,cooing fireman withstand grotesque year
Tonia.Saberio34_01,Tonia.Saberio34,juvenile toothpaste fix odd breakfast
Lottie,Eustatius_01,Lottie,Eustatius,Lottie.Eustatius22@funmail.com""")
    return filename

def write_duplicate_status(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
Brandea.Miguela45_937,Brandea.Miguela45,rare wren overdo macho circle
Abbi.Nicholas17_248,Abbi.Nicholas17,sharp flock peel astonishing loaf
Wendi.Anjali23_260,Wendi.Anjali23,talented notebook vanish huge discussion
Wendi.Anjali23_260,Wendi.Anjali23,talented notebook vanish huge discussion""")
    return filename

def write_good_status(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
Channa.Formica62_01,Channa.Formica62,thinkable existence hug aback sky
Joanna.Publius21_01,Joanna.Publius21,cooing fireman withstand grotesque year
Tonia.Saberio34_01,Tonia.Saberio34,juvenile toothpaste fix odd breakfast
Lottie.Eustatius_01,Lottie.Eustatius22,Lottie.Eustatius22@funmail.com""")
    return filename


class TestUserStatusCollection(unittest.TestCase):
    '''
    user_status.py UserStatusCollection Testing
    '''

    def setUp(self):
        '''Setup for userstatus_collection testing'''

        with socialnetwork_model.start_dataframe_db('sqlite:///:memory:'):
            self.empty_user_collection = main.init_user_collection()
            self.empty_status_collection = main.init_status_collection()
            self.full_user_collection = test_users.create_full_user_collection()
            self.full_status_collection = create_full_status_collection(self.full_user_collection)

    @classmethod
    def setUpClass(cls):
        cls.bad_status_header_file = write_bad_header_status(HERE / "bad_status_header.csv")
        cls.bad_status_file = write_bad_status(HERE / "bad_status.csv")
        cls.good_status_file = write_good_status(HERE / "good_status.csv")
        cls.duplicate_status_file = write_duplicate_status(HERE / "duplicate_status.csv")
        cls.good_users_file = test_users.write_good_users(HERE / "good_users.csv")


    @classmethod
    def tearDownClass(cls):
        os.remove(HERE / "bad_status_header.csv")
        os.remove(HERE / "bad_status.csv")
        os.remove(HERE / "good_status.csv")
        os.remove(HERE / "duplicate_status.csv")
        os.remove(HERE / "good_users.csv")

    def test_search_status(self):
        '''
        search_user successful test
        '''
        status = main.search_status('cbarker12_00001',
                                    self.full_status_collection)

        assert status['STATUS_ID']== 'cbarker12_00001'
        assert status['USER_ID'] == 'cbarker12'
        assert status['STATUS_TEXT'] == "Code is finally compiling"


    def test_search_status_fail(self):
        '''
        search_status unsuccessful test
        '''
        status = main.search_status('NotThere_00001',
                                self.empty_status_collection)

        assert status is None


    def test_add_status(self):
        '''
        add_status successful test
        '''
        new_status = main.add_status('cbarker12',
                                    'New_Status0001',
                                    "This is a status update",
                                    self.empty_status_collection, self.full_user_collection)

        assert new_status is True
        assert main.search_status('New_Status0001',\
            self.empty_status_collection)['STATUS_ID'] == 'New_Status0001'
        assert main.search_status('New_Status0001',\
            self.full_status_collection)['USER_ID'] == 'cbarker12'
        assert main.search_status('New_Status0001',\
            self.empty_status_collection)['STATUS_TEXT'] == "This is a status update"


    def test_add_status_duplicate(self):
        '''
        add_status test for user already in collection
        '''
        new_status = main.add_status('fjones34',
                                     'fjones34_00001',
                                     "Perfect weather for a hike",
                                     self.full_status_collection, self.full_user_collection)

        assert new_status is False

    def test_add_status_nouserid(self):
        '''
        add_status test for user already in collection
        '''
        new_status = main.add_status('NotThere',
                                     'fjones34_00001',
                                     "Perfect weather for a hike",
                                     self.full_status_collection, self.full_user_collection)

        assert new_status is False

    def test_delete_status(self):
        '''
        delete_user successful test
        '''

        delete_status = main.delete_status('bwinkle678_00003', self.full_status_collection)

        assert delete_status is True
        assert main.search_status('bwinkle678_00003', self.full_status_collection) is None

    def test_delete_status_not_there(self):
        '''
        delete_user unsuccessful test
        '''
        delete_status = main.delete_status('Tay_00001', self.full_status_collection)

        assert delete_status is False
        assert main.search_status('Tay_00001', self.full_status_collection) is None

    def test_delete_status_with_userid(self):
        '''
        delete_user successful test
        '''

        delete_user = main.delete_user('bwinkle678',\
            self.full_status_collection, self.full_user_collection)

        assert delete_user is True
        assert main.search_status('bwinkle678_00003', self.full_status_collection) is None

    def test_modify_status(self):
        '''
        modify_status successful test
        '''

        mod_status = main.update_status\
            ('fjones34_00001', 'fjones34', "This is an updated status",\
                self.full_status_collection)

        assert mod_status is True
        assert main.search_status('fjones34_00001', \
            self.full_status_collection)['STATUS_ID'] == 'fjones34_00001'
        assert main.search_status('fjones34_00001', \
            self.full_status_collection)['USER_ID'] == 'fjones34'
        assert main.search_status('fjones34_00001', \
            self.full_status_collection)['STATUS_TEXT'] == "This is an updated status"

    def test_modify_status_not_found(self):
        '''
        modify_status unsuccessful test
        '''

        mod_status = main.update_status\
            ('dave03_00004', 'dave03', "This is an updated status", self.full_status_collection)

        assert mod_status is False
        assert main.search_status('dave03_00004',\
            self.full_status_collection) is None

    def test_load_status_no_file(self):
        """
        Tests when there is no file with the input name
        """

        result = main.load_status_updates("badfile.csv", self.empty_status_collection)

        assert result is False

    def test_load_status_duplicate(self):
        """
        Tests when there is duplicate data in the csv when loading
        """
        result = main.load_status_updates(self.duplicate_status_file, self.empty_status_collection)

        assert result is False

    def test_load_status_updates(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserStatusCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """
        main.load_users(self.good_users_file, self.empty_user_collection)
        result = main.load_status_updates(self.good_status_file, self.empty_status_collection)

        assert result is True
        assert main.search_status('Channa.Formica62_01',\
            self.empty_status_collection)['STATUS_ID'] == 'Channa.Formica62_01'
        assert main.search_status('Joanna.Publius21_01',\
            self.empty_status_collection)['STATUS_ID']  == 'Joanna.Publius21_01'
        assert main.search_status('Tonia.Saberio34_01',\
            self.empty_status_collection)['STATUS_ID']  == 'Tonia.Saberio34_01'
        assert main.search_status('Lottie.Eustatius_01',\
            self.empty_status_collection)['STATUS_ID']  == 'Lottie.Eustatius_01'

    def test_load_status_bad(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserStatusCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """
        main.load_users(self.good_users_file, self.empty_user_collection)
        result = main.load_status_updates(self.bad_status_file, self.empty_status_collection)

        assert result is False
        assert main.search_status('Channa.Formica62_01',\
            self.empty_status_collection) is None
        assert main.search_status('Joanna.Publius21_01',\
            self.empty_status_collection)  is None
        assert main.search_status('Tonia.Saberio34_01',\
            self.empty_status_collection)  is None
        assert main.search_status('Lottie,Eustatius_01',\
            self.empty_status_collection)  is None

    def test_load_status_bad_header(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserStatusCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """
        main.load_users(self.good_users_file, self.empty_user_collection)
        result = main.load_status_updates(self.bad_status_header_file, self.empty_status_collection)

        assert result is False
        assert main.search_status('Channa.Formica62_01',\
            self.empty_status_collection) is None
        assert main.search_status('Joanna.Publius21_01',\
            self.empty_status_collection)  is None
        assert main.search_status('Tonia.Saberio34_01',\
            self.empty_status_collection)  is None
        assert main.search_status('Lottie,Eustatius_01',\
            self.empty_status_collection)  is None
