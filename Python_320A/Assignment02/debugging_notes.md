These notes are to record the debugging process in 320A assignment 2. for menu.py

1. Moved .upper() to user_selection input to allow for more flexible user inputs.
2. All of the functions need either a user or status_collection as an input. Those were added respectively.
3. In def update_user(user_collection):, the main.update_user function was missing a user_collection as input. That was added.
4. Main function statement needs to be able to pass either the status or user_collection to the right program. A multiple OR if statement was added.
5. menu.search_user function if not statement changed to result.user_id from result.name
6. menu.search_status function result.user_id: changed to result.status_id:
7. Quit option needs its on elsif statement since it doesn't need with user or status collection
8. Received pylint error W0621 'redefined-outer-name' for user_collection and status_collection, I believe this is telling me to not use the same     variable names as those in the function portion of the document. So main_ was added to the front to clear this for both variables.