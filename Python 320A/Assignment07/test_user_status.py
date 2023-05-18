'''Test File for user_status.py'''
# pylint: disable=redefined-outer-name, unused-import

import pytest
from user_status import UserStatusCollection
from main import start_mongo
from test_users import empty_db

@pytest.fixture
def full_status_db():
    """
    provides a full datbase of both users and status for testing
    NOTE: you can have multiple databases in one mongo instance
          So we can use one for testing that's separate from the
          operational one
    """
    client = start_mongo()
    client.drop_database('test_database')

    database = client.test_database
    user_collect = database.users
    status_collect = database.status

    # user collection
    user_collect.insert_one({'_id': "Tay_01", 'user_name': "Tay", \
        'user_last_name': "Pham", 'email': "Tay@email.com"})
    user_collect.insert_one({'_id': "James_01", 'user_name': "James", \
        'user_last_name': "bear", 'email': "Bear@email.com"})
    user_collect.insert_one({'_id': "KiKi_01", 'user_name': "Ki", \
        'user_last_name': "Ki", 'email': "Ki@email.com"})


    # status collection
    status_collect.insert_one({'_id': "Tay_01_0001", 'user_id': "Tay_01", \
        'status_text': "This is test text."})
    status_collect.insert_one({'_id': "Tay_01_0002", 'user_id': "Tay_01", \
        'status_text': "Second one for Tay_01."})
    status_collect.insert_one({'_id': "James_01_0001", 'user_id': "James_01", \
        'status_text': "More Test Text."})
    status_collect.insert_one({'_id': "James_01_0002", 'user_id': "James_01", \
        'status_text': "Even more text for James_01."})
    status_collect.insert_one({'_id': "KiKi_01_0001", 'user_id': "KiKi_01", \
        'status_text': "KiKi was a good dog."})

    yield database

    client.close()

def test_init_empty_status_collection(empty_db):
    '''initialize test for user collections'''

    status_col = UserStatusCollection(empty_db)

    assert len(status_col) == 0

def test_init_full_status_collection(full_status_db):
    '''initialize test for user collections'''

    status_col = UserStatusCollection(full_status_db)

    assert len(status_col) == 5

def test_search_status(full_status_db):
    '''
    search_status successful test
    '''

    status_col = UserStatusCollection(full_status_db)
    test_id = 'Tay_01_0001'
    status = status_col.search_status(status_id = test_id)

    assert status.status_id == "Tay_01_0001"
    assert status.user_id == "Tay_01"
    assert status.status_text == "This is test text."


def test_search_status_fail(full_status_db):
    '''
    search_status unsuccessful test
    '''
    status_col = UserStatusCollection(full_status_db)
    test_id = 'not_there'
    status = status_col.search_status(status_id = test_id)

    assert status.status_id is None
    assert status.user_id is None
    assert status.status_text is None

def test_add_status(empty_db):
    '''
    add_status successful test
    '''
    status_col = UserStatusCollection(empty_db)
    result = status_col.add_status('New_01_0001', 'New_01', 'New Status Text.')

    assert result is True
    assert status_col.search_status(status_id = 'New_01_0001').status_id == 'New_01_0001'


def test_add_user_duplicate(full_status_db):
    '''
    add_status when there is already a user of that name
    '''
    status_col = UserStatusCollection(full_status_db)
    result = status_col.add_status("KiKi_01_0001", "KiKi_01", 'iKi was a good dog.')

    assert result is False
    assert len(status_col) == 5

def test_delete_status(full_status_db):
    '''Test deletion of a status'''

    status_col = UserStatusCollection(full_status_db)
    test_id = "KiKi_01_0001"
    result = status_col.delete_status(status_id = test_id)

    assert result is True
    assert status_col.search_status(status_id = "KiKi_01_0001").status_id is None
    assert len(status_col) == 4


def test_delete_status_not_found(full_status_db):
    '''Test deletion of a status who doesn't exist'''

    status_col = UserStatusCollection(full_status_db)
    test_id = "not_there_0001"
    result = status_col.delete_status(status_id = test_id)

    assert result is False
    assert status_col.search_status(status_id = "not_there_0001").status_id is None
    assert len(status_col) == 5

def test_modify_status(full_status_db):
    '''Test modification of a user'''

    status_col = UserStatusCollection(full_status_db)

    result = status_col.modify_status("James_01_0002", \
        "New_James_01", "New_Even more text for James_01")

    assert result is True

    status = status_col.search_status(status_id = "James_01_0002")

    assert status.status_id == "James_01_0002"
    assert status.user_id == "New_James_01"
    assert status.status_text == "New_Even more text for James_01"


def test_modify_status_not_found(full_status_db):
    '''Test modification of a user that does not exist'''

    status_col = UserStatusCollection(full_status_db)

    result = status_col.modify_status("not_there","New_James", "New_bear")

    assert result is False
    assert status_col.search_status(status_id = "not_there").status_id is None
