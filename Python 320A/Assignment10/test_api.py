'''
Testing for api.py
'''

import pytest
import os
import shutil
import api
from menu import HERE, TEMP
from test_user_picture import generate_pictures

@classmethod
def setup_class(cls):
    """setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    api.initialize_test()


@classmethod
def teardown_class(cls):
    """teardown any state that was previously setup with a call to
    setup_class.
    """
    if os.path.isdir(TEMP) is True:
        shutil.rmtree(TEMP)
    if os.path.isfile(HERE /'socialnetwork.db') is True:
        os.remove(HERE/'socialnetwork.db')


@pytest.fixture()
def testapp():
    """
    fixture for test application
    """
    api.app.config.update({
        "TESTING": True,
    })

    yield api.app

@pytest.fixture()
def client(testapp):
    """
    fixture for client
    """
    return testapp.test_client()


def test_sync_get_null(client):

    response = client.get("/differences")
    data = response.get_json()

    assert data is None

# def test_sync_get_extra_disk(client):

#     location = ['tay1/dog', 'tay/cat', 'tay1/dog/pig', 'tay/sheep/mice']
#     pic = ['0000000001.png','0000000002.png','0000000003.png','0000000004.png']

#     generate_pictures(location, pic)

#     response = client.get("/differences")
#     data = response.get_json()

#     assert len(data) == 4

def test_sync_get_extra_db(client):

    shutil.rmtree(HERE / "temp/cbarker12/bike")
    shutil.rmtree(HERE / "temp/fjones34/bird")

    response = client.get("/differences")
    data = response.get_json()

    assert len(data) == 2

