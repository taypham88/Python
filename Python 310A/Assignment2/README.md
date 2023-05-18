# Assignment 2: Capturing data exercises

## Objectives
In this assignment we will develop an application that captures data
for use in a Pyhton program.
## Instructions
1. Start by reviewing the problem described below.
1. When you are familiar with the requirements, start to plan how you
will write the Python code.
1. As you write the code be sure to test it frequently.
1. Submit your complete assignment when you are sure you have implemented
all of the requirements.

### Basics
Let’s build an automated interviewer! The purpose of this Python program is 
to operate in a welcome booth at the Seattle Python Users conference. All 
delegates will be expected to line up at one of the many terminals and enter 
their details into the program you are going to write.

The program will ask each of the following questions and turn, and will 
display the answer. For example, it asks “what is your name” and it displays 
“your name is Fred”. But be creative if you wish!

Here are the questions:
1. What is your name?
1. What is your conference ID?
1. Which organization do you represent?
1. What is your email address?
1. State any food preferences?

The program will then display the following:

Select which of the following sessions you wish to attend – enter y or n

And it will then display the following questions:

Python for beginners
Database development with Python
Python for data science
Advanced Python for application developers

Automated interviewer – improvements.

The automated interviewer serves its purpose from the perspective of the 
user of the program. But the mingling of questions and answers makes it a 
little messy to maintain.

Redesign the program so that the list of questions is stored in a tuple. 
Then, all the questions are in one place and it becomes really easy to add 
one.

But what about the answers? How can we record the answer to every question 
without making any changes to the program other than adding a new question 
(or removing an existing question) from the tuple?

Look at the notes about tuples and lists and see if you can rewrite the 
program so that a simple change to the question tuple is all that is needed 
to record all the relevant answers
