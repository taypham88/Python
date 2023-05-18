# '''
# Tests menu.py the main driver code for Social Network
# '''

# import unittest
# import os
# from pathlib import Path
# import mock
# from socialnetwork_model import StatusTable, UsersTable, start_database
# import menu
# import test_users
# import test_userstatus
# import main

# HERE = Path(__file__).parent

# class TestMenuUsers(unittest.TestCase):
#     '''
#     menu.py User related function testing
#     '''
#     def setUp(self):

#         self.database = start_database(':memory:')
#         self.empty_user_collection, self.empty_status_collection = menu.initialize(self.database)

#     @classmethod
#     def setUpClass(cls):
#         cls.users_file = test_users.write_good_users(HERE / "testing_acct.csv")
#         cls.status_file = test_userstatus.write_good_status(HERE / "testing_status.csv")

#     @classmethod
#     def tearDownClass(cls):
#         os.remove(HERE / "testing_acct.csv")
#         os.remove(HERE / "testing_status.csv")

#     def test_load_users(self):
#         '''
#         test load users function from menu.py
#         '''

#         with mock.patch('builtins.input', side_effect = ['testing_acct.csv']):
#             menu.load_users(self.database)

#         assert UsersTable.select().count() == 4

#     def test_load_users_bad_file(self):
#         '''
#         test load users function from menu.py
#         '''

#         with mock.patch('builtins.input', side_effect = ["do_not_exist.csv"]):
#             menu.load_users(self.database)

#         assert UsersTable.select().count() == 0

#     def test_add_user(self):
#         '''
#         test for add_user function from menu.py
#         '''
#         responses = ('NewID', 'NewEmail@gmail.com', 'NewName', 'NewLast')

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.add_user(self.empty_user_collection)

#         assert main.search_user('NewID', self.empty_user_collection).user_id == 'NewID'
#         assert main.search_user('NewID', self.empty_user_collection).email == 'NewEmail@gmail.com'
#         assert main.search_user('NewID', self.empty_user_collection).user_name == 'NewName'
#         assert main.search_user('NewID', self.empty_user_collection).user_last_name == 'NewLast'

#     def test_add_user_fail(self):
#         '''
#         test for add_user's failure case from menu.py
#         '''
#         responses = ('NewID', 'NewEmail@gmail.com', 'NewName', 'NewLast', \
#             'NewID', 'NewEmail@gmail.com', 'NewName', 'NewLast')

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.add_user(self.empty_user_collection)
#             menu.add_user(self.empty_user_collection)

#         assert UsersTable.select().count() == 1
#         assert main.search_user('NewID', self.empty_user_collection).user_id == 'NewID'

#     def test_update_user(self):
#         '''
#         test for update_user function from menu.py
#         '''

#         responses = ('Channa.Formica62', 'NewEmail@gmail.com', 'NewName', 'NewLast')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.update_user(self.empty_user_collection)


#         assert main.search_user('Channa.Formica62',\
#             self.empty_user_collection).email == 'NewEmail@gmail.com'
#         assert main.search_user('Channa.Formica62',\
#             self.empty_user_collection).user_name == 'NewName'
#         assert main.search_user('Channa.Formica62',\
#             self.empty_user_collection).user_last_name == 'NewLast'

#     def test_update_user_failed(self):
#         '''
#         test for update_user's failure case from menu.py
#         '''
#         responses = ('NotThere', 'NewEmail@gmail.com', 'NewName', 'NewLast')

#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.update_user(self.empty_user_collection)

#         assert main.search_user('NotThere', self.empty_user_collection).user_id is None

#     def test_search_user(self):
#         '''tests search user function in menu.py'''

#         responses = ('Tonia.Saberio34')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.search_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.


#     def test_search_user_failed(self):
#         '''tests failed case for search user function in menu.py'''

#         responses = ('Not_There')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.search_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.

#     def test_delete_user(self):
#         '''tests delete user function in menu.py'''

#         responses = ('Joanna.Publius21')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.delete_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.
#     def test_delete_user_fail(self):
#         '''tests delete user function in menu.py'''

#         responses = ('Not_There')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.delete_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.

#     def test_load_status_updates(self):
#         '''test load status updates function from menu.py'''

#         responses = ['testing_acct.csv','status_updates.csv']

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.load_users(self.database)
#             menu.load_status_updates(self.database)

#         # no assert check, this is to see that there is no exceptions that occur once ran.

#     def test_update_status_failed(self):
#         '''test load status updates function from menu.py'''

#         responses = ['testing_acct.csv','status_updates.csv']

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.load_users(self.database)
#             menu.load_status_updates(self.database)

#         # no assert check, this is to see that there is no exceptions that occur once ran.

#     def test_search_user(self):
#         '''tests search user function in menu.py'''

#         responses = ('Tonia.Saberio34')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.search_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.


#     def test_search_user_failed(self):
#         '''tests failed case for search user function in menu.py'''

#         responses = ('Not_There')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.search_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.

#     def test_delete_user(self):
#         '''tests delete user function in menu.py'''

#         responses = ('Joanna.Publius21')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.delete_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.
#     def test_delete_user_fail(self):
#         '''tests delete user function in menu.py'''

#         responses = ('Not_There')
#         main.load_users('testing_acct.csv', self.database)

#         with mock.patch('builtins.input', side_effect = responses):
#             menu.delete_user(self.empty_user_collection)

#         # no assert check, this is to see that there is no exceptions that occur once ran.
