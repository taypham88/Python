# Tay Pham 11/07/2021
# Assignment 4: Validating and exception of input data
# Part 1, collecting and storing data

# import os and pandas interfaces
import os
import pandas as pd
from cerberus import Validator
from datetime import date
# Date used for later in report
today = date.today()

# check if file is there, if not it will print an error message and stop the program
if os.path.isfile("InterviewQuestions.csv") is False:
	print("Question file does not exist")
	quit()
 
# Function to accept yes or no inputs in various formats and return a boolean True or False
def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Please enter y or n")
        answer = input(question + "(y/n):").lower().strip()
    if answer[0] == "y":
        return True
    else:
        return False

# Character length schema for cerberus. Question needs to be between 10 to 30 characters long. used in while loop question validation
# Email format schema for cerberus. Checks if its in the email@email.com format
char = Validator({'characterlength': {'min': 10, 'max': 30}})
email = Validator({'email' : {'type' : 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}})

# Two list to record the failed validation and inputs, len(list) will give you a count
cv_list = []
ev_list = []

# Action New Text for section
questions_sorted =[]
questions_sorted = pd.read_csv("InterviewQuestions.csv").sort_values('sequencenumber', ascending = True).reset_index(drop=True)
dict_questions =[]
dict_questions = questions_sorted.to_dict(orient = 'records') # turns dataframe into a list of dictionaries. index is dropped but the questions are sorted. 

# Print into statement for the user
intro_statement = ["Hello, we are about to ask you a series of questions regarding your vist.", "You will get a chance to review each question."]
for statements in intro_statement:
	print(statements)
 

# This for loop will ask the user a series of questions to validate the questions that will be asked. User is allowed to edit the questions and remove questions. 
# There is a character length limit for newly entered questions (not a practical length).
for dict in dict_questions:
    answer_question = yes_or_no(f"Would you like to answer the question: '{dict['question']}'?")
    if answer_question == True:
        change_question = yes_or_no(f"Would you like to edit the question: '{dict['question']}'?")
        if change_question == True:
           question_input = input(f"What would you like to change the question to? (Note there is a 10 to 30 character limit.)").strip()
           # checks for the character validation
           while char.validate({'characterlength' : len(question_input)}) == False:
               cv_list.append(question_input)
               print("Please enter a question between 10 and 30 characters long")
               question_input = input(f"What would you like to change the question to? (Note there is a 10 to 30 character limit.)").strip()
           if char.validate({'characterlength' : len(question_input)}) == True:
               verify_change = yes_or_no(f"Are you sure you would like to change the question to: '{question_input}'?")
               if verify_change == True:
                   dict['question'] = question_input
               elif verify_change == False:
                   print("Question was not changed")                 
    elif answer_question == False:
        delete_question = yes_or_no("are you sure you want to delete this question?")
        if delete_question == True:
        	dict['deletedflag'] = True
        else:
            print('Question was not removed.')
               
        
# This for loop creates a new dictionary called answers. It will consist of the questionid and answer input from the user. 
report_dict =[]
for dict in dict_questions:
    if dict['deletedflag'] == False:
        if dict['booleanquestion'] == False:
            if dict['questionid'] == 130:
                email_answer = input(dict['question']).strip()
                while email.validate({'email' : email_answer}) == False: # checks for the email validation
                    ev_list.append(email_answer)
                    print('Please enter a valid email format email@email.com')
                    email_answer = input(dict['question']).strip()
                if email.validate({'email' : email_answer}) == True:
                    dict.update({'answer': email_answer})
                    report_dict.append(dict)
            else:
                dict.update({'answer': input(dict['question']).strip()})
                report_dict.append(dict)
                if dict['questionid'] == 100: # store off the name.
                    name = dict['answer']
        elif dict['booleanquestion'] == True:
            boolean_input = yes_or_no(dict['question'])
            if boolean_input == True:
                dict.update({'answer': True})
                report_dict.append(dict)
            elif boolean_input == False:
                dict.update({'answer': False})
                report_dict.append(dict)
    else:
        dict.update({'answer' : 'Not asked'})
        report_dict.append(dict)
        if dict['questionid'] == 100: #store off the name if question was asked. 
            name = 'N/A'

# The following sections deal with generating the report. Prints an intro, lists the questions and answers and then the validation report.

# Intro           
report_intro = [f"Conference report for {name}", f"{today}", "\n", "The following is a summary of questions asked and their answers:"]
with open('Interview Report.csv','w', encoding='utf-8') as report:
    for line in report_intro:
        report.write(line)
        report.write('\n')
        
with open('Interview Report.csv','a', encoding='utf-8') as report:
	for dict in report_dict:
		if dict['deletedflag'] == False:
			report.write(f"\t The Question '{dict['question']}' with id '{dict['questionid']}' was answered with '{dict['answer']}'.")
			report.write('\n')
		else:
			report.write(f"\t The Question '{dict['question']}' with id '{dict['questionid']}' was declined by the user.")
			report.write('\n')

with open('Interview Report.csv','a', encoding='utf-8') as report:
	report.write('\n')
	report.write("This section discusses validation attempts for the character length check and the email format check:")
	report.write('\n')
	report.write(f"\t The character length check occured {len(cv_list)} times and cconsisted of {cv_list}.")
	report.write('\n')
	report.write(f"\t The email check occured {len(ev_list)} times and consisted of {ev_list}.")
 
# close the report  
report.close()  	