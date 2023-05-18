'''Test File for user.py'''
# pylint: disable=redefined-outer-name

import pytest
from users import UserCollection
from main import start_mongo

@pytest.fixture
def empty_db():
    """
    provides an empty database to use for testing
    NOTE: you can have multiple databases in one mongo instance
          So we can use one for testing that's separate from the
          operational one
    """
    client = start_mongo()
    client.drop_database('test_database')

    database = client.test_database

    yield database

    client.close()

@pytest.fixture
def full_db():
    """
    provides a full database of users for testing
    NOTE: you can have multiple databases in one mongo instance
          So we can use one for testing that's separate from the
          operational one
    """
    client = start_mongo()
    client.drop_database('test_database')

    database = client.test_database
    collect = database.users

    collect.insert_one({'_id': "Tay_01", 'user_name': "Tay", \
        'user_last_name': "Pham", 'email': "Tay@email.com"})
    collect.insert_one({'_id': "James_01", 'user_name': "James", \
        'user_last_name': "bear", 'email': "Bear@email.com"})
    collect.insert_one({'_id': "KiKi_01", 'user_name': "Ki", \
        'user_last_name': "Ki", 'email': "Ki@email.com"})

    # now pass it to the test
    yield database

    # probably not required as the object will get cleaned
    # when deleted, but still a good practice
    client.close()

def test_init_empty_user_collection(empty_db):
    '''initialize test for user collections'''

    user_col = UserCollection(empty_db)

    assert len(user_col) == 0

def test_init_full_user_collection(full_db):
    '''initialize test for user collections'''

    user_col = UserCollection(full_db)

    assert len(user_col) == 3

def test_search_user(full_db):
    '''
    search_user successful test
    '''

    user_col = UserCollection(full_db)

    test_id = 'Tay_01'
    user = user_col.search_user(user_id = test_id)

    assert user.user_id == "Tay_01"
    assert user.email  == "Tay@email.com"
    assert user.user_name == "Tay"
    assert user.user_last_name == "Pham"

def test_search_user_fail(full_db):
    '''
    search_user unsuccessful test
    '''
    user_col = UserCollection(full_db)

    test_id = 'not_there'
    user = user_col.search_user(user_id = test_id)

    assert user.user_id is None
    assert user.email  is None
    assert user.user_name is None
    assert user.user_last_name is None

def test_add_user(empty_db):
    '''
    add_user successful test
    '''
    user_col = UserCollection(empty_db)

    result = user_col.add_user('New_01', 'New_first', 'New_last', 'New@email.com')

    assert result is True
    assert user_col.search_user(user_id = 'New_01').user_id == 'New_01'


def test_add_user_duplicate(full_db):
    '''
    add_user when there is already a user of that name
    '''
    user_col = UserCollection(full_db)

    result = user_col.add_user("KiKi_01", "Ki", 'Ki', "Ki@email.com")

    assert result is False
    assert len(user_col) == 3

def test_delete_user(full_db):
    '''Test deletion of a user'''
    user_col = UserCollection(full_db)

    test_id = "KiKi_01"
    result = user_col.delete_user(user_id = test_id)

    assert result is True
    assert user_col.search_user(user_id = "KiKi_01").user_id is None


def test_delete_user_not_found(full_db):
    '''Test deletion of a user who doesn't exist'''
    user_col = UserCollection(full_db)

    test_id = "not_there"
    result = user_col.delete_user(user_id = test_id)

    assert result is False
    assert user_col.search_user(user_id = "not_there").user_id is None

def test_modify_user(full_db):
    '''Test modification of a user'''

    user_col = UserCollection(full_db)

    result = user_col.modify_user("James_01", "New_Bear@email.com", "New_James", "New_bear")

    assert result is True

    user = user_col.search_user(user_id = "James_01")

    assert user.user_id == "James_01"
    assert user.email  == "New_Bear@email.com"
    assert user.user_name == "New_James"
    assert user.user_last_name == "New_bear"
    assert len(user_col) == 3


def test_modify_user_not_found(full_db):
    '''Test modification of a user that does not exist'''

    user_col = UserCollection(full_db)

    result = user_col.modify_user("not_there", "New_Bear@email.com", "New_James", "New_bear")

    assert result is False
    assert user_col.search_user(user_id = "not_there").user_id is None
