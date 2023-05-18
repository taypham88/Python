# Assignment 6

## Time to complete this assignment:

You have two weeks for this assignment.

## Motivation:

With your newly acquired Python skills you have been asked by a friend who 
runs a small business to develop an application to keep track of her employees.

There will be an estimate 40-50 employees at any one time; your friend, as business
owner, will be the sole user of the system. It is fine that it will run as an app
that is launched from the terminal and will use text based input and output.

You are going to develop that system. It will be able to record basic employee 
details, like name, address, Social Security number (SSN), date of birth, job title,
start date and end date. It will store these details in a csv (Comma-separated files,
which you may have used on spreadsheet software) file on disk, from where
it can also load them, so the employee details can be amended. The system must make 
appropriate use of validation for the data entered (check for missing fields, invalid
values, etc.), and must also be able to trap major errors (things that will make your
program crash), at least by reporting a meaningful message.

The system must be able to produce a list of all employees who are currently 
employed, and a list of all employess who have left on the last month. Both 
lists must be sorted by employee id number.

The system needs to be able to display reminders to schedule an annual review 
with an employee 3 months prior to their individual review date. This can just 
be shown on the screen for the purpose of this assignment.

Because this system is used to store data about people it is very important 
that it is tested well, using automated testing techniques.

## Here is what you need to do:

1. Develop the data capture and data amendment functionality. Capture 
additional information to that specified above, based on what you think will 
be useful or needed.
1. Make sure the data is validated, so data entry errors can be prevented as 
much as possible.
1. Ensure that data is stored in a csv file and can be retrieved.
1. Build a menu so the system is easy to use.
1. Ensure each employee has a unique id.
1. Make use of formatting techniques to ensure that information reported to 
the screen is well laid out and easy to understand. More specifically, each 
row of data should be printed out on a new line and have a separator of some 
sort in between each item (ideally, it will look tabular).
1. Use automated testing to validate the system behaves as intended.
1. Carefully consider data needs that are implied by the functionality 
described (such as for triggering reports).
1. Be sure to commit to local git frequently and use a virtual environment.

## Submission:

Your submission should include the following:

1. All Python (.py) files, including tests, that you developed.
1. A sample csv file with some employee data in it.
1. Any other files required to successfully run your code.
1. Run `git log > history.txt` in the terminal from your project root 
directory to show how you have committed regularly.
1. Be sure to submit through git, using a pull request from a branch called *development*. 
1. You also need to upload your code to Canvas, uploading it as a pull request.
1. In Canvas, add a comment to your submission with a link to your pull request.

Your submission **should not** include your virtual environment. To ensure this, create your
virtual environment in the parent folder of your assignment repository.

## Tips

1. Be creative! Use this as an opportunity to reflect on everything you have 
learned so far and apply it to application development.
1. Use your time well, two weeks might seem like a lot, but you will run out of time if you
wait too much to get started. At the end of the first week, you should have the first
*draft* of your project, so that you can devote the second week fixing potential crashes
and adding any missing features.
