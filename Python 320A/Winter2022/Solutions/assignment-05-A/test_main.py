"""
tests for the main driver code of the Social Network
"""

# less picky about style for test code
# pylint: disable=C0103 # to allow short names in the tests
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=duplicate-code

import os
# import io
import unittest
from pathlib import Path
# from unittest import mock

from loguru import logger

import main
from users import UserCollection
from user_status import UserStatusCollection

HERE = Path(__file__).parent

good_account_file = HERE / "accounts_small.csv"
bad_account_file = HERE / "accounts_bad.csv"

SAMPLE_USERS_DATA = [{'user_id': 'cbarker12',
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

SAMPLE_STATUS_DATA = [{'user_id': 'cbarker12',
                 'status_id': 'st12345',
                 'status_text': 'A simple message from user: cbarker12'
                 },
                {'user_id': 'fjones34',
                 'status_id': 'st12355',
                 'status_text': 'A simple message from user: fjones34'
                 },
                {'user_id': 'bwinkle678',
                 'status_id': 'st12455',
                 'status_text': 'A simple message from user: bwinkle678'
                 },
                {'user_id': 'cbarker12',
                 'status_id': 'st55555',
                 'status_text': 'A second simple message from user: cbarker12'
                 },
                ]

def setup_logger():  # pragma: no cover
    """
    Set up the logger for the test runs
    """
    # create a logfile with today's date
    logfilename = "logfile_for_test_runs.txt"
    logger.add(logfilename,
               mode='a',  # append, so the file sticks around
               encoding='utf-8',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               retention=3  # keep the last 3 logfile
               )


setup_logger()


def write_bad_header(filename):
    """
    writes an accounts csv file with a bad header
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,,NAME,LASTNAME
evmiles97, eve.miles@uw.edu,Eve,Miles
dave03,david.yuen@gmail.com, David,Yuen
""")
    return filename

def write_bad_row(filename):
    """
    writes an accounts csv file with a bad row
    (one two few elements)
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
evmiles97, eve.miles@uw.edu,Miles
dave03,david.yuen@gmail.com, David,Yuen
""")
    return filename

class TestUserCollection(unittest.TestCase):
    """
    tests for the UserCollection functions
    """

    def setUp(self):
        self.mongo = main.MongoDBConnection()
        # note: using a different database here
        self.database = self.mongo.connection.TestDatabase
        self.database.drop_collection('users')
        self.database.drop_collection('user_status')

        # populate the user_collection
        self.full_user_collection = main.init_user_collection(self.database)
        for user in SAMPLE_USERS_DATA:
            self.full_user_collection.add_user(**user)

    def tearDown(self):
        self.database.drop_collection('users')
        self.database.drop_collection('user_status')
        self.mongo.connection.close()

    @classmethod
    def setUpClass(cls):
        """
        create a couple data files with bad data
        """
        cls.bad_header_file = write_bad_header(HERE / "bad_header.csv")
        cls.bad_row_file = write_bad_row(HERE / "bad_row.csv")

    @classmethod
    def tearDownClass(cls):
        os.remove(HERE / "bad_header.csv")
        os.remove(HERE / "bad_row.csv")

    def test_init_user_collection(self):
        """
        Make sure you get a new UserCollection with test data in it

        Really a test of the fixture
        """
        uc = main.init_user_collection(self.database)

        self.assertIsInstance(uc, UserCollection)
        self.assertEqual(len(uc), 3)

    def test_search_user_there(self):
        """
        tests that a user can be found in the collection
        """
        user = main.search_user('fjones34',
                                self.full_user_collection)

        print(user)
        assert user['_id'] == 'fjones34'

    def test_search_user_not_there(self):
        """
        tests that a user that isn't there gets a None user
        """
        user = main.search_user('somejunk',
                                self.full_user_collection)

        assert user is None

    def test_add_user(self):
        """
        tests adding a user to a user_collection
        """
        uc = self.full_user_collection

        status = main.add_user('xxxxx',
                               'this@that.com',
                               'cbarker',
                               'Barker',
                               uc)

        assert status is True

        print(main.search_user('xxxxx', uc))
        # self.user_id = user_id
        # self.email = email
        # but did it actually add the user?
        assert main.search_user('xxxxx', uc)['_id'] == 'xxxxx'
        assert main.search_user('xxxxx', uc)['email'] == 'this@that.com'

    def test_add_user_already_there(self):
        """
        tests adding a user to a user_collection
        """
        uc = self.full_user_collection

        status = main.add_user('cbarker12',
                               'this@something.com',
                               'fjones',
                               'Jones',
                               uc)

        assert status is False
        # but did it overwrite the user?
        assert main.search_user('cbarker12', uc)['user_name'] != 'fjones'

    def test_load_users_good(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection

        If successful, it it returns True.

        This uses a "good" csv file
        """
        uc = self.full_user_collection

        result = main.load_users(good_account_file, uc)

        # It should have loaded correctly and returned True
        assert result is True
        # did the data actually get loaded?
        assert main.search_user('dave03', uc)['_id'] == 'dave03'

    # def test_load_users_bad(self):
    #     """
    #     tests : Opens a CSV file with user data and
    #             adds it to an existing instance of
    #             UserCollection

    #         - Returns False if there are any errors
    #         (such as empty fields in the source CSV file)

    #     This uses a "bad" csv file
    #     """
    #     uc = self.full_user_collection

    #     result = main.load_users(bad_account_file, uc)

    #     # It should have failed loading and returned False
    #     assert result is False
    #     # did the data at the error line actually get loaded?
    #     assert main.search_user('dave03', uc).user_id is None
    #     # did the data before the error line get loaded?
    #     # Note: this wasn't clear in the specifcation, but
    #     #       it's a bad idea to load some of the data, but not
    #     #       all -- there would be no way to know the state of
    #     #       the database
    #     assert main.search_user('evmiles97', uc).user_id is None

    # def test_load_users_bad_header(self):
    #     """
    #     tests : Opens a CSV file with user data and
    #             adds it to an existing instance of
    #             UserCollection

    #         - Returns False if there are any errors
    #         (such as empty fields in the source CSV file)

    #     This uses a "bad" csv file
    #     """
    #     uc = self.full_user_collection

    #     result = main.load_users(self.bad_header_file, uc)

    #     # It should have failed loading and returned False
    #     assert result is False

    # def test_load_users_bad_row(self):
    #     """
    #     Returns False if there are any errors
    #     (such as empty fields in the source CSV file)

    #     This uses a csv file with a bad row
    #     """
    #     uc = self.full_user_collection

    #     result = main.load_users(self.bad_row_file, uc)

    #     # It should have failed loading and returned False
    #     assert result is False

    #     # it should not have created a database
    #     assert not uc.database

    def test_delete_user(self):
        uc = self.full_user_collection
        uid = 'fjones34'

        assert main.delete_user(uid, uc) is True

        assert main.search_user(uid, uc) is None

    def test_delete_user_not_there(self):
        uc = self.full_user_collection
        uid = 'xxxxxxx'
        assert main.delete_user(uid, uc) is False

    def test_update_user(self):
        uc = self.full_user_collection
        user_id = 'bwinkle678'
        email = 'this@that.com'
        user_name = 'fbarnes'
        user_last_name = 'Barnes'

        result = main.update_user(user_id,
                                  email,
                                  user_name,
                                  user_last_name,
                                  uc)

        assert result is True

        user = main.search_user(user_id, uc)
        assert user['email'] == email
        assert user['user_name'] ==user_name
        assert user['user_last_name'] ==user_last_name

    def test_update_user_not_there(self):
        uc = self.full_user_collection
        user_id = 'xxxxx'
        email = 'this@that.com'
        user_name = 'fbarnes'
        user_last_name = 'Barnes'
        result = main.update_user(user_id, email, user_name, user_last_name, uc)

        assert result is False

class TestStatusCollection(unittest.TestCase):
    """
    tests for the StatusCollection functions
    """
    def setUp(self):
        self.mongo = main.MongoDBConnection()
        # note: using a different database here
        self.database = self.mongo.connection.TestDatabase
        self.database.drop_collection('users')
        self.database.drop_collection('user_status')

        # user collection needs to be there for status_collection to work
        # populate the user_collection
        self.full_user_collection = main.init_user_collection(self.database)
        for user in SAMPLE_USERS_DATA:
            self.full_user_collection.add_user(**user)

        # populate the status_collection
        self.full_status_collection = main.init_status_collection(self.database)
        for stat in SAMPLE_STATUS_DATA:
            self.full_status_collection.add_status(**stat)


    def tearDown(self):
        self.database.drop_collection('users')
        self.database.drop_collection('user_status')
        self.mongo.connection.close()

    # def setUp(self):
    #     self.full_status_collection = main.init_status_collection()
    #     self.full_status_collection = make_full_status_collection()
    #     # self.bad_header_file = write_bad_header(HERE / "bad_header.csv")
    #     # self.bad_header_file = write_bad_header(HERE / "bad_header.csv")

    # @classmethod
    # def setUpClass(cls):
    #     cls.bad_header_file = write_bad_header(HERE / "bad_header.csv")

    # @classmethod
    # def tearDownClass(cls):
    #     os.remove(HERE / "bad_header.csv")

    def test_init_status_collection(self):
        """make sure you get a new, empty UserStatusCollection"""
        sc = main.init_status_collection(self.database)

        self.assertIsInstance(sc, UserStatusCollection)
        self.assertEqual(len(sc), 4)

    def test_search_status(self):
        """
        checks that a valid status is found, and is the right one
        """

        status_id = 'st12345'
        result = main.search_status(status_id, self.full_status_collection)

        assert result['_id'] == status_id

    def test_search_status_not_there(self):
        """
        checks that a valid status is found, and is the right one
        """

        status_id = 'xxxxx'
        result = main.search_status(status_id, self.full_status_collection)

        assert result is None

    def test_delete_status_not_there(self):
        sc = self.full_status_collection
        stat_id = 'xxxxxx'
        result = main.delete_status(stat_id, sc)

        assert result is False

    def test_delete_status_there(self):
        sc = self.full_status_collection
        stat_id = 'st12355'
        result = main.delete_status(stat_id, sc)
        assert result

        # check that it was really deleted
        result = main.search_status(stat_id, sc)
        assert result is None

    def test_update_status_not_there(self):
        sc = self.full_status_collection
        stat_id = '1111111'
        user_id = '12345'
        status_text = 'new status text'
        result = main.update_status(stat_id, user_id, status_text, sc)
        assert result is False

    def test_update_status_there(self):
        sc = self.full_status_collection
        stat_id = 'st12355'
        user_id = '12345'
        status_text = 'new status text'
        result = main.update_status(stat_id, user_id, status_text, sc)
        assert bool(result) is True

        # check if the update "took"
        status = main.search_status(stat_id, sc)
        assert status['_id'] == stat_id
        assert status['status_text'] == 'new status text'

    def test_add_status(self):
        sc = self.full_status_collection

        sid = 'xxxxxx'
        main.add_status(sid, 'yyyyy', 'jsut some text', sc)

        assert main.search_status(sid, sc) is None

    def test_add_status_already_there(self):
        sc = self.full_status_collection
        sid = 'st12345'

        result = main.add_status('yyyyy', sid, 'just some text', sc)

        assert result is False

        assert main.search_status(sid, sc)['user_id'] != 'yyyyy'

    def test_load_status_good(self):
        """
        tests : Opens a CSV file with user data and
                adds it to an existing instance of
                UserCollection

        If successful, it it returns True.

        This uses a "good" csv file
        """
        sc = self.full_status_collection
        uc = self.full_user_collection

        # have to load users first
        main.load_users(HERE / "accounts_small.csv", uc)
        result = main.load_status_updates(HERE / "status_updates_small.csv", sc)

        # It should have loaded correctly and returned True
        assert result is True

        # did the data actually get loaded?
        assert main.search_status('evmiles97_00001', sc)['user_id'] == 'evmiles97'

    # @mock.patch('builtins.open')
    # def test_load_status_bad_header(self, mocked_open):
    #     """
    #     a csv file with a bad header should fail
    #     """
    #     mocked_open.return_value = io.StringIO("STATUS_ID,USER_IDSTATUS_TEXT")

    #     sc = self.full_status_collection
    #     result = main.load_status_updates(HERE / "status_updates_small.csv", sc)
    #     # It should have not loaded correctly
    #     assert result is False

#     @mock.patch('builtins.open')
#     def test_load_status_missing_field(self, mocked_open):
#         """
#         a csv file with a bad header should fail
#         """
#         mocked_open.return_value = io.StringIO("""STATUS_ID,USER_ID,STATUS_TEXT
# evmiles97_00001,evmiles97,"Code is finally compiling"
# dave03_00001dave03,"Sunny in Seattle this morning"
# evmiles97_00002,evmiles97,"Perfect weather for a hike"
# """)

#         sc = self.full_status_collection
#         result = main.load_status_updates(HERE / "status_updates_small.csv", sc)
#         # It should have loaded correctly and returned True
#         assert result is False

#         # the StatusCollection should be empty
#         assert not sc.database

#     @mock.patch('builtins.open')
#     def test_load_status_empty_field(self, mocked_open):
#         """
#         a csv file with a bad header should fail
#         """
#         mocked_open.return_value = io.StringIO("""STATUS_ID,USER_ID,STATUS_TEXT
# evmiles97_00001,evmiles97,"Code is finally compiling"
# dave03_00001, dave03,"Sunny in Seattle this morning"
# evmiles97_00002, ,"Perfect weather for a hike"
# """)

#         sc = self.full_status_collection
#         result = main.load_status_updates(HERE / "status_updates_small.csv", sc)
#         # It should have loaded correctly and returned True
#         assert result is False

#         # the StatusCollection should be empty
#         assert len(sc) == 0
