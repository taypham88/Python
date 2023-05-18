'''
Tests Main.py the main driver code for Social Network
'''

import os
from pathlib import Path
import unittest

import main
from users import UserCollection
from user_status import UserStatusCollection

HERE = Path(__file__).parent
good_account_file = HERE / "accounts.csv"
good_status_file = HERE / "status_updates.csv"

def create_full_user_collection():
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

    u_c = main.init_user_collection()
    for user in users:
        u_c.add_user(**user)
    return u_c

def create_full_status_collection():
    """
    UserStatusCollection, instead of drilling into other file's code to check the initial creation.
    it is best to create the user instances here. This was copied in the
    class solution.
    """
    status = [{'status_id': 'evmiles97_00001',
              'user_id': 'evmiles97',
              'status_text': "Code is finally compiling",
              },
             {'status_id': 'dave03_00001',
              'user_id': 'dave03',
              'status_text': "Sunny in Seattle this morning",
              },
             {'status_id': 'evmiles97_00002',
              'user_id': 'cevmiles97',
              'status_text': "Perfect weather for a hike",
              }]

    u_s = main.init_status_collection()
    for user in status:
        u_s.add_status(**user)
    return u_s

def write_bad_header_accounts(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,,NAME,LASTNAME
evmiles97, eve.miles@uw.edu,Eve,Miles
dave03,david.yuen@gmail.com, David,Yuen""")
    return filename

def write_bad_accounts(filename):
    """
    Creates a files for accounts.csv with bad user data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
evmiles97,eve.miles@uw.edu,Eve,Miles
dave03,david.yuen@gmail.com,,Yuen""")
    return filename

def write_bad_accounts_extra(filename):
    """
    Creates a files for accounts.csv with bad extra data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
evmiles97,eve.miles@uw.edu,Eve,Miles,extra,extra,extra
dave03,david.yuen@gmail.com,,Yuen""")
    return filename

def write_bad_header_status(filename):
    """
    Creates a files for status_updates.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write(""",,
evmiles97_00001,evmiles97,"Code is finally compiling"
dave03_00001,dave03,"Sunny in Seattle this morning"
evmiles97_00002,evmiles97,"Perfect weather for a hike""")
    return filename

def write_bad_status(filename):
    """
    Creates a files for status_updates.csv with bad data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
evmiles97_00001,evmiles97,"Code is finally compiling"
dave03_00001,dave03,"Sunny in Seattle this morning"
evmiles97_00002,,"Perfect weather for a hike""")
    return filename

def write_bad_status_extra(filename):
    """
    Creates a files for status_updates.csv with bad extra data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
evmiles97_00001,evmiles97,"Code is finally compiling"
dave03_00001,dave03,"Sunny in Seattle this morning",extra,extra
evmiles97_00002,,"Perfect weather for a hike""")
    return filename

# main test case
class TestUserCollection(unittest.TestCase):
    '''
    user.py UserCollection Testing
    '''

    def setUp(self):
        self.empty_user_collection = main.init_user_collection()
        self.full_user_collection = create_full_user_collection()

    @classmethod
    def setUpClass(cls):
        cls.bad_user_header_file = write_bad_header_accounts(HERE / "bad_user_header.csv")
        cls.bad_accounts_file = write_bad_accounts(HERE / "bad_accounts.csv")
        cls.bad_accounts_extra_file = write_bad_accounts_extra(HERE / "bad_accounts_extra.csv")

    @classmethod
    def tearDownClass(cls):
        os.remove(HERE / "bad_user_header.csv")
        os.remove(HERE / "bad_accounts.csv")
        os.remove(HERE / "bad_accounts_extra.csv")

    def test_init_user_collection(self):
        '''initialize test for user collections'''

        self.assertIsInstance(self.empty_user_collection, UserCollection)
        self.assertEqual(len(self.empty_user_collection.database), 0)

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
        user = main.search_user('Tay100',
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

    def test_add_user_dublicate(self):
        '''
        add_user test for user already in collection
        '''
        new_user = main.add_user('cbarker12',
                               'this@something.com',
                               'fjones',
                               'Jones',
                               self.full_user_collection)

        assert new_user is False
        assert main.search_user('cbarker12', self.full_user_collection).user_name != 'fjones'

    def test_load_users_good(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """

        result = main.load_users(good_account_file, self.empty_user_collection)

        # It should have loaded correctly and returned True
        assert result is True
        # did the data actually get loaded?
        assert main.search_user('dave03', self.empty_user_collection).user_id == 'dave03'

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

        # It should have failed loading and returned False
        assert result is False
        # did the data at the error line actually get loaded?
        assert main.search_user('dave03', self.empty_user_collection).user_id is None

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

        # It should have failed loading and returned False
        assert result is False

        assert not self.empty_user_collection.database
        assert main.search_user('evmiles97', self.empty_user_collection).user_id is None

    def test_load_users_bad_extra(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_users(self.bad_accounts_extra_file, self.empty_user_collection)

        # It should have failed loading and returned False
        assert result is False

        assert not self.empty_user_collection.database
        assert main.search_user('evmiles97', self.empty_user_collection).user_id is None

    def test_update_user(self):
        '''
        update_user successful test
        '''

        mod_user = main.update_user\
            ('cbarker12', 'updated@gmail.com', 'Dave', 'Y', self.full_user_collection)

        assert mod_user is True
        assert main.search_user('cbarker12', \
            self.full_user_collection).user_id == 'cbarker12'
        assert main.search_user('cbarker12', \
            self.full_user_collection).email == 'updated@gmail.com'
        assert main.search_user('cbarker12', \
            self.full_user_collection).user_name == 'Dave'
        assert main.search_user('cbarker12', \
            self.full_user_collection).user_last_name == 'Y'

    def test_update_user_not_found(self):
        '''
        update_user unsuccessful test
        '''

        mod_user = main.update_user\
            ('Tay100', 'tay@gmail.com', 'Tay', 'Pham', self.full_user_collection)

        assert mod_user is False
        assert main.search_user('Tay100', \
            self.full_user_collection).user_id is None

    def test_delete_user(self):
        '''
        delete_user successful test
        '''

        delete_user = main.delete_user('cbarker12', self.full_user_collection)

        assert delete_user is True
        assert main.search_user('cbarker12', self.full_user_collection).user_id is None

    def test_delete_user_not_there(self):
        '''
        delete_user unsuccessful test
        '''
        delete_user = main.delete_user('Tay', self.full_user_collection)

        assert delete_user is False
        assert main.search_user('Tay', self.full_user_collection).user_id is None

    def test_save_users(self):
        """
        tests saving the user collection to a csv file
        """

        filename = HERE / "temp_accounts.csv"
        result = main.save_users(filename, self.full_user_collection)

        assert result is True

        # reload it to see if it worked
        # this istough -- as this test depends on the load_users
        # working. You could look at the generated csv file.

        main.load_users(filename, self.empty_user_collection)

        assert main.search_user('bwinkle678', self.empty_user_collection).user_id == 'bwinkle678'
        os.remove(HERE /  "temp_accounts.csv")

    def test_save_users_bad_file(self):
        """
        should fail if the file path is bad
        """
        result = main.save_users(Path() \
            / 'non' / 'existant' / 'file.csv', self.full_user_collection)

        assert result is False


class TestUserStatusCollection(unittest.TestCase):
    '''
    user_status.py UserStatusCollection Testing
    '''

    def setUp(self):
        self.empty_status_collection = main.init_status_collection()
        self.full_status_collection = create_full_status_collection()

    @classmethod
    def setUpClass(cls):
        cls.bad_status_header_file = write_bad_header_status(HERE / "bad_status_updates_header.csv")
        cls.bad_status_file = write_bad_status(HERE / "bad_status_updates.csv")
        cls.bad_status_extra_file = write_bad_status_extra(HERE / "bad_status_updates_extra.csv")

    @classmethod
    def tearDownClass(cls):
        os.remove(HERE / "bad_status_updates_header.csv")
        os.remove(HERE / "bad_status_updates.csv")
        os.remove(HERE / "bad_status_updates_extra.csv")

    def test_init_status_collection(self):
        '''
        initialize test for status collections
        '''

        self.assertIsInstance(self.empty_status_collection, UserStatusCollection)
        self.assertEqual(len(self.empty_status_collection.database), 0)

    def test_search_status(self):
        '''
        search_user successful test
        '''
        status = main.search_status('evmiles97_00001',
                                self.full_status_collection)

        assert status.status_id == 'evmiles97_00001'
        assert status.user_id == 'evmiles97'
        assert status.status_text == "Code is finally compiling"


    def test_search_status_fail(self):
        '''
        search_status unsuccessful test
        '''
        status = main.search_status('Tay100_00001',
                                self.full_status_collection)

        assert status.status_id is None
        assert status.user_id is None
        assert status.status_text is None

    def test_add_status(self):
        '''
        add_status successful test
        '''
        new_status = main.add_status('Tay100',
                                    'Tay100_00001',
                                    "This is a status update",
                                    self.full_status_collection)

        assert new_status is True
        assert main.search_status('Tay100_00001',\
            self.full_status_collection).status_id == 'Tay100_00001'
        assert main.search_status('Tay100_00001',\
            self.full_status_collection).user_id == 'Tay100'
        assert main.search_status('Tay100_00001',\
            self.full_status_collection).status_text == "This is a status update"

    def test_add_status_dublicate(self):
        '''
        add_status test for user already in collection
        '''
        new_status = main.add_status('Tay100',
                                     'evmiles97_00001',
                                     "This is a dublicate status",
                                     self.full_status_collection)

        assert new_status is False
        assert main.search_status('evmiles97_00001',\
            self.full_status_collection).user_id != 'Tay100'

    def test_load_status_updates_good(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
        If successful, it it returns True.
        This uses a "good" csv file
        """

        result = main.load_status_updates(good_status_file, self.empty_status_collection)

        # It should have loaded correctly and returned True
        assert result is True
        # did the data actually get loaded?
        assert main.search_status('evmiles97_00001', \
            self.empty_status_collection).status_id == 'evmiles97_00001'

    def test_load_status_bad(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_status_updates(self.bad_status_file, self.empty_status_collection)

        # It should have failed loading and returned False
        assert result is False
        # did the data at the error line actually get loaded?
        assert main.search_status('evmiles97_00001', self.empty_status_collection).status_id is None


    def test_load_status_bad_header(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_status_updates(self.bad_status_header_file, self.empty_status_collection)

        # It should have failed loading and returned False
        assert result is False

        assert not self.empty_status_collection.database
        assert main.search_status('evmiles97', self.empty_status_collection).status_id is None

    def test_load_status_bad_extra(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection
            - Returns False if there are any errors
            (such as empty fields in the source CSV file)
        This uses a "bad" csv file
        """

        result = main.load_status_updates(self.bad_status_extra_file, self.empty_status_collection)

        # It should have failed loading and returned False
        assert result is False

        assert not self.empty_status_collection.database
        assert main.search_status('evmiles97', self.empty_status_collection).status_id is None

    def test_modify_status(self):
        '''
        modify_status successful test
        '''

        mod_status = main.update_status\
            ('dave03_00001', 'dave03_new', "This is an updated status", self.full_status_collection)

        assert mod_status is True
        assert main.search_status('dave03_00001', \
            self.full_status_collection).status_id == 'dave03_00001'
        assert main.search_status('dave03_00001', \
            self.full_status_collection).user_id == 'dave03_new'
        assert main.search_status('dave03_00001', \
            self.full_status_collection).status_text == "This is an updated status"

    def test_modify_status_not_found(self):
        '''
        modify_status unsuccessful test
        '''

        mod_status = main.update_status\
            ('dave03_00004', 'dave03_new', "This is an updated status", self.full_status_collection)

        assert mod_status is False
        assert main.search_status('dave03_00004', self.full_status_collection).user_id is None

    def test_delete_user(self):
        '''
        delete_user successful test
        '''

        delete_status = main.delete_status('evmiles97_00001', self.full_status_collection)

        assert delete_status is True
        assert main.search_status('evmiles97_00001', self.full_status_collection).status_id is None

    def test_delete_user_not_there(self):
        '''
        delete_user unsuccessful test
        '''
        delete_status = main.delete_status('Tay_00001', self.full_status_collection)

        assert delete_status is False
        assert main.search_status('Tay_00001', self.full_status_collection).status_id is None

    def test_save_status(self):
        """
        tests saving the user collection to a csv file
        """

        filename = HERE / "temp_status_updates.csv"
        result = main.save_status_updates(filename, self.full_status_collection)

        assert result is True

        # reload it to see if it worked
        # this istough -- as this test depends on the load_users
        # working. You could look at the generated csv file.

        main.load_status_updates(filename, self.empty_status_collection)

        assert main.search_status('evmiles97_00001', \
            self.empty_status_collection).status_id == 'evmiles97_00001'
        os.remove(HERE / "temp_status_updates.csv")

    def test_save_status_bad_file(self):
        """
        should fail if the file path is bad
        """
        result = main.save_status_updates(Path() \
            / 'non' / 'existant' / 'file.csv', self.full_status_collection)

        assert result is False
