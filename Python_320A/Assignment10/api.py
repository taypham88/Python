'''
File contains the api connection and generating functions for the social network.
'''
from flask import Flask, jsonify
from flask_restful import Resource, Api
import main
import user_picture
import user_status
import socialnetwork_model
import menu
from test_userstatus import create_full_status_collection
from test_users import create_full_user_collection
from test_user_picture import create_full_picture_collection

app = Flask(__name__)
api = Api(app)

class ListUsers(Resource):
    '''
    Runs search function on PH_DB['UserStatusTable'] and displays
    info to url /users
    '''
    def get(self):

        search= list(user_status.UserStatusCollection.\
        search_status(status_collection))

        return jsonify(search)

class ListPictures(Resource):
    '''
    Runs search function on PH_DB['PictureTable'] and displays
    info to url /images
    '''
    def get(self):

        search= list(user_picture.PictureCollection.\
        search_user_picture(picture_collection))

        return jsonify(search)

class SyncReport(Resource):
    '''
    Runs reconcile_image from main and displays
    differences between images stored on disk to those in the database
    to the url /differences.
    '''
    def get(self):
        _, diff = main.reconcile_images(picture_collection)
        if diff is None:
            return jsonify(None)
        return jsonify(list(diff))


with socialnetwork_model.start_dataframe_db() as database:
    user_collection, status_collection\
        , picture_collection = menu.initialize()

def initialize_test():
    user_collection = create_full_user_collection()
    picture_collection = create_full_picture_collection(user_collection)
    status_collection = create_full_status_collection(user_collection)

# item 1 on assignment 10, list all users status
api.add_resource(ListUsers, "/users")
# item 2 on assignment 10, list all  users picture data
api.add_resource(ListPictures, "/images")
# item 3 on assignment 10, compare pictures on disk to database
api.add_resource(SyncReport, "/differences")

if __name__ == "__main__":

    initialize_test()
    app.run(port="5002")

    database.close()
