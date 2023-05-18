# Assignment 3: Storing and retrieving data

## Objectives
In this assignment you will learn how to store the results of your
automated interview, and also retrieve the results.

## Instructions
1. Start by reviewing the problem described below.
1. When you are familiar with the requirements, start to plan how you will write the Python code.
1. As you write the code be sure to test it frequently.
1. Submit your complete assignment when you are sure you have implemented all of the requirements.

### Basics

Our app is now quite useful. We can manage and amend the questions easily. 
But now we need to be able to add features to save and load data.
First we will deal with the questions.

Each question that we need to get answered will be stored in a file, and 
reloaded from the file when the program starts running.

We will build a new program to prompt for the questions, and store them in 
the file. Later, we will work on having the automated interviewer program 
read the questions from this file. 

The file will store the question, a question id number that identifies the 
question throughout its life (creation to delete), a sequence number, 
indicating the order in which each question should be asked, and finally a 
flag that indicates if the questions is no longer to be used (a “deleted” 
flag which is True if the question is not to be used. For now that will default to False).

The file will look something like this:

questionid, sequencenumber, question,deletedflag

10,1,”What is your email”, False

Write the new program to capture the questions.

Now we will allow Automated Interviewer to load the questions from the 
question file so it can display and use them.
Automated Interviewer must not assume the questions are in the correct 
sequence, so it needs to sort them before starting to use them.
Run Automated Interviewer and make sure it works. Change the order of the 
questions, delete some and add some and check it all works as intended.

Finally we are going to modify Automated Interviewer to store the answers to 
the questions, and then write a new program print them.

The file will look something like this:

questionid,nameofpersoninterviewed,answer

2,”Andy”,”akmiles@uw.edu”

When the file is stored successfully create a new py file that will create a 
clearly formatted report that shows the name of the interviewee, and each 
question followed by its respective answer.
