# Assignment 4: Validating data

## Objectives
In this assignment you will learn how to validate data in your
automated interview.

## Instructions
1. Start by reviewing the entire problem described below.
1. When you are familiar with the requirements, start to plan how you will write the Python code.
1. As you write the code be sure to test it frequently.
1. Submit your complete assignment when you are sure you have implemented all of the requirements.

### Basics
You will recall that from last weeks' assignment we have two files:

Firstly

questionid, sequencenumber, question,deletedflag

10,1,”What is your email”, False

And then

questionid,nameofpersoninterviewed,answer

2,”Andy”,”akmiles@uw.edu”

In this weeks' assignment we are going to add validation and exception tracking code to last
week's submission.

Here are the steps you need to follow. We start with the questions file.

1. Write new functionality that will read through the questions file one record at a time.
1. For each record, ask the user to validate that the question is correct. 
1. "Correct" means the user is happpy with the wording.
1. ALso, the question must be between 10 and 30 character long.
3.Display a message that
asks the user if they wish to correct the question. Then capture corrected value as needed.
1. Also ask the user if the question is needed, or if it should be deleted. Validate the
users repsonse and allow them to retry entering an answer.
1. If the user wants to delete the question, ask if they are sure. Validate the user's input, 
and then either delete or move on.
1. Introduce validations using a similar pattern for at least 3 more questions.

HINT: be sure to get the validations in the correct sequence, so the flow makes sense to the user. Also,
you may wish to open the current file for reading, and create a new file, that gets "flipped"
back to the original filename when done.

BE VERY CAREFUL TO MAINTAIN RELATIONSHIPS BETWEEN EXISTING QUESTIONS AND THEIR ANSWERS.

Now to the answers file:

1. Add code to make sure that the email address is provided and that it is in a valid
email format. 
1. Make sure that if the email fails any validation that the incorrect value is displayed, and
that the user is asked to provide the email address again.
1. Verify that answers have been provided to each question. If an answer is missing, reprompt
the user and save the answer.
1. Make sure you delete any "dangling" answers; that is, answers that no longer have a question because 
2. the question was deleted.

HINT: take care to make sure that you identifty the answer that corresponds to its associated question.
Give some thought as to how you can do this.

When all validation is done, produce a report that shows the number of questions that were validated successfuly,
the number of answers that were validated successfully, the number of questions that failed validation, and the 
before and after values for each (that is, the invlaid and corrected values), the number of answers that failed validation, and the 
before and after values for each (that is, the invlaid and corrected values).
Also list the questions that were deleted.
