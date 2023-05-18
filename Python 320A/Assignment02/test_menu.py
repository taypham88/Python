'''
Tests menu.py the main driver code for Social Network
'''

import unittest
from pathlib import Path
import mock

import menu
import main

HERE = Path(__file__).parent
good_account_file = HERE / "accounts.csv"
good_status_file = HERE / "status_updates.csv"

class TestMenuUsers(unittest.TestCase):
    '''
    menu.py User related function testing
    '''
    def setUp(self):
        self.user_collection = main.init_user_collection()


    def test_load_users(self):
        '''
        test load users function from menu.py
        '''

        with mock.patch('builtins.input', side_effect = ['accounts.csv']):
            menu.load_users(self.user_collection)

        assert main.search_user('dave03', self.user_collection).user_id == 'dave03'

    def test_add_user(self):
        '''
        test for add_user function from menu.py
        '''
        responses = ('NewID', 'NewEmail@gmail.com', 'NewName', 'NewLast')

        with mock.patch('builtins.input', side_effect = responses):
            menu.add_user(self.user_collection)

        assert main.search_user('NewID', self.user_collection).user_id == 'NewID'

    def test_add_user_fail(self):
        '''
        test for add_user's failure case from menu.py
        '''
        responses = ('dave03', 'NewEmail@gmail.com', 'NewName', 'NewLast')

        with mock.patch('builtins.input', side_effect = responses):
            assert menu.add_user(self.user_collection) is None

    def test_update_user(self):
        '''
        test for update_user function from menu.py
        '''
        responses = ('dave03', 'NewEmail@gmail.com', 'NewName', 'NewLast')
        main.load_users(good_account_file, self.user_collection)

        with mock.patch('builtins.input', side_effect = responses):
            menu.update_user(self.user_collection)

        # Unknown failure
        assert main.search_user('dave03', self.user_collection).email == 'NewEmail@gmail.com'

    def test_update_user_failed(self):
        '''
        test for update_user's failure case from menu.py
        '''
        responses = ('NotThere', 'NewEmail@gmail.com', 'NewName', 'NewLast')

        main.load_users(good_account_file, self.user_collection)

        with mock.patch('builtins.input', side_effect = responses):
            assert menu.update_user(self.user_collection) is None

class TestMenuStatus(unittest.TestCase):
    '''
    menu.py Status related function testing
    '''
    def setUp(self):
        self.status_collection = main.init_status_collection()

    def test_load_status_updates(self):
        '''test load status updates function from menu.py'''

        with mock.patch('builtins.input', side_effect = ['status_updates.csv']):
            menu.load_status_updates(self.status_collection)

        assert main.search_status('dave03_00001',
                                  self.status_collection).status_id == 'dave03_00001'

    def test_add_status(self):
        '''
        test for add_status function from menu.py
        '''
        responses = ('NewID', 'NewStatus_00001', 'New Status Text')

        with mock.patch('builtins.input', side_effect = responses):
            menu.add_status(self.status_collection)

        assert main.search_status('NewStatus_00001', \
            self.status_collection).status_id == 'NewStatus_00001'


    def test_add_status_fail(self):
        '''
        test for add_status's failure case from menu.py
        '''
        responses = ('dave03', 'NewStatus_00001', 'New Status Text')

        with mock.patch('builtins.input', side_effect = responses):
            assert menu.add_status(self.status_collection) is None
