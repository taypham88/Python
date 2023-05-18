# Tay Pham 10/28/2021
# Assignment 3: Storing and retrieving data 
# Part 1, collecting and storing data

# import os and pandas interfaces
import os
import pandas as pd

# check if file is there, if not it will print an error message and stop the program
if os.path.isfile("InterviewQuestions.csv") is False:
	print("Question file does not exist")
	quit()

# Questions are stored in a csv file that has questionid, sequencenumber,question, deletedflag as headers. 
# read in csv file 
# Sort the questions by sequencenumber
# reindexed questions_sorted, drop = true means throw away old index
questions_sorted =[]
questions_sorted = pd.read_csv("InterviewQuestions.csv").sort_values('sequencenumber', ascending = True).reset_index(drop=True)

print(questions_sorted)# check dataframe values in terminal

# empty answers list and create dataframe for csv file output
answers=[]
df_answers = pd.DataFrame(columns = ["questionid","nameofpersoninterviewed","answer"])

# loop to collect answers to questions with deleteflag not set to true. If it is set to true then 
# an answer of N/A is recorded. This includes the name. Anything above the 6th question is a Y/N response to the classes. 
# for Y/N questions, invalid inputs will be set to No. 
for i in range(len(questions_sorted)):
	if questions_sorted.loc[i,"deletedflag"] == False:
		if questions_sorted.loc[i,"sequencenumber"] < 6:  
			answers.append(input(questions_sorted.loc[i,"question"]).strip())
		else:
			place_holder= input(questions_sorted.loc[i,"question"])
			if place_holder.strip().upper() == "Y":
				answers.append("Yes")
			elif place_holder.strip().upper() == "N":
				answers.append("No")
			else:
				print("invalid Input, Choice Taken as No")
				answers.append("No")
	else:
		answers.append("N/A")

print(answers)# check dataframe values in terminal

# loop to build/append to answers output dataframe. answers[0] is where name is stored. 
for i in range(len(questions_sorted)):
	df_answers.loc[i] = [questions_sorted.loc[i,"questionid"], answers[0], answers[i]]

print(df_answers)# check dataframe values in terminal

# prints answers to another csv file for storage
df_answers.to_csv('InterviewAnswers.csv', encoding='utf-8', index=False)

