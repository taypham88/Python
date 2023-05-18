'''
Tests user_picture.py for Social Network
'''

import unittest
import shutil
import os
from pathlib import Path
import socialnetwork_model
import main
import test_users

TEMP_Folder = Path('temp/')

def generate_pictures(location, pic):
    '''
    Generates pictures on disk.
    '''
    for i, picture in enumerate(pic):
        temp = Path('temp/'+ location[i])
        temp.mkdir(parents=True, exist_ok=True)
        with open(temp / picture[i], 'a', encoding='utf-8') as newfile:
            newfile.close()

def create_full_picture_collection(user_collection):
    """
    UserStatusCollection, instead of drilling into other file's code to check the initial creation.
    it is best to create the user instances here. This was copied in the
    class solution.
    """
    status = [{'USER_ID': 'cbarker12',
              'TAGS': "dog yellow",
              },
             {'USER_ID': 'cbarker12',
              'TAGS': "bike red",
              },
             {'USER_ID': 'fjones34',
              'TAGS': "bird green",
              },
             {'USER_ID': 'fjones34',
              'TAGS': "blue bat",
              }]

    picture_collection = main.init_picture_collection()
    for item in status:
        main.add_picture(item['USER_ID'],\
            item['TAGS'], picture_collection, user_collection)
    return  picture_collection


class TestPictureCollection(unittest.TestCase):
    '''
    user_picture.py PictureCollection Testing
    '''

    def setUp(self):
        '''Setup for picture_collection testing'''

        with socialnetwork_model.start_dataframe_db('sqlite:///:memory:'):
            self.empty_user_collection = main.init_user_collection()
            self.empty_picture_collection = main.init_picture_collection()
            self.full_user_collection = test_users.create_full_user_collection()
            self.full_picture_collection = create_full_picture_collection(self.full_user_collection)

    def tearDown(self):
        '''Removes temp/ directory for pictures.'''

        shutil.rmtree(TEMP_Folder)

    def test_search_user_picture(self):
        '''
        search_user_picture successful test
        '''
        pictures = main.search_user_picture('cbarker12',
                                    self.full_picture_collection)

        assert len(pictures) == 2

        assert pictures[0]['USER_ID'] == 'cbarker12'
        assert pictures[0]['PICTURE_ID'] == "0000000001.png"
        assert pictures[0]['TAGS'] == "#dog#yellow"
        assert pictures[0]['LOCATION'] == "cbarker12/dog/yellow"
        assert pictures[1]['USER_ID'] == 'cbarker12'
        assert pictures[1]['PICTURE_ID'] == "0000000002.png"
        assert pictures[1]['TAGS'] == "#bike#red"
        assert pictures[1]['LOCATION'] == "cbarker12/bike/red"

    def test_search_user_picture_fail(self):
        '''
        search_user_picture failed test
        '''
        pictures = main.search_user_picture('notthere',
                                    self.full_picture_collection)

        assert pictures is None

    def test_add_picture(self):
        '''
        add_picture successful test
        '''
        result = main.add_picture('cbarker12',\
            'orange cow', self.full_picture_collection, self.full_user_collection)

        assert result is True
        assert main.search_user_picture('cbarker12'\
            ,self.full_picture_collection)[2]['PICTURE_ID'] == "0000000005.png"
        assert main.search_user_picture('cbarker12'\
            ,self.full_picture_collection)[2]['TAGS'] == '#cow#orange'
        assert main.search_user_picture('cbarker12'\
            ,self.full_picture_collection)[2]['LOCATION'] == 'cbarker12/cow/orange'
        assert os.path.isfile('temp/cbarker12/cow/orange/0000000005.png') is True

    def test_add_picture_fail(self):
        '''
        add_picture unsuccessful
        '''
        result = main.add_picture('notthere',\
            'orange cow', self.full_picture_collection, self.full_user_collection)

        assert result is False

    def test_reconcile_images(self):
        '''
        reconcile_images no duplicates test
        '''
        sim, diff = main.reconcile_images(self.full_picture_collection)

        assert len(diff) == 0
        assert len(sim) == 4

    def test_reconcile_images_diff(self):
        '''
        reconcile_images no duplicates test
        '''
        location = ['tay/dog', 'tay/cat', 'tay/dog/pig', 'tay/sheep/mice']
        pic = ['0000000001.png','0000000002.png','0000000003.png','0000000004.png']

        generate_pictures(location, pic)
        sim, diff = main.reconcile_images(self.full_picture_collection)

        assert len(diff) == 4
        assert len(sim) == 4

def test_list_user_images():
    '''
    Searches disk for pictures matching user_id
    '''
    location = ['tay1/dog', 'tay/cat', 'tay1/dog/pig', 'tay/sheep/mice']
    pic = ['0000000001.png','0000000002.png','0000000003.png','0000000004.png']

    generate_pictures(location, pic)
    result = main.list_user_images('tay1')

    assert len(result) == 2
    shutil.rmtree(TEMP_Folder)

def test_list_user_images_null():
    '''
    Searches disk for pictures matching user_id. with no results returned.
    '''
    location = ['tay1/dog', 'tay/cat', 'tay1/dog/pig', 'tay/sheep/mice']
    pic = ['0000000001.png','0000000002.png','0000000003.png','0000000004.png']

    generate_pictures(location, pic)
    result = main.list_user_images('notthere')

    assert len(result) == 0
    shutil.rmtree(TEMP_Folder)
