'''
Classes for pictures in socialnetwork
'''
# pylint: disable=logging-fstring-interpolation
import logging
from pathlib import Path
import socialnetwork_model
import logging_setup_function as log

class PictureCollection():
    '''
    Contains a collection of picture objects
    '''

    def __init__(self):

        self.picturetable = socialnetwork_model.initialize_picturetable()

    @log.log_decorator
    def add_picture(self, user_id, hashtag, location):
        '''
        Adds a new picture to the collection
        '''

        pic_id = str(len(self.picturetable)+1).zfill(10)+ '.png'

        # Write file to disk in folder called temp/
        temp = Path('temp/'+ location)
        temp.mkdir(parents=True, exist_ok=True)
        with open(temp / pic_id, 'a', encoding='utf-8') as newfile:
            newfile.close()

        self.picturetable.insert(PICTURE_ID= pic_id, \
            USER_ID=user_id, TAGS=hashtag, LOCATION = location)
        return True

    def search_user_picture(self, user_id=None):
        '''
        Searches for all pictures in pictures table associated with user_id
        '''

        if user_id is None:
            user = self.picturetable.find() # This returns all entries
        else:
            user = self.picturetable.find(USER_ID = user_id)
        if len(user) == 0:
            logging.info(f"search_user_picture DoesNotExist, User {user_id} not found")
            return None
        return user
