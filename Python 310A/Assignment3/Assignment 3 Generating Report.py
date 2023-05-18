# Tay Pham 10/28/2021
# Assignment 3: Storing and retrieving data 
# Part 2, Generating Report of answers

# Print to a csv file: the user's name, the date along with all questions, its ID and their answers. 
# Import csv,os,pandas and datetime modules
import os
import pandas as pd
from datetime import date
# Date used for later in report
today = date.today()

# check if files are there and if not print error
if os.path.isfile("InterviewQuestions.csv") is False:
    print("Question file does not exist")
    quit()

if os.path.isfile("InterviewAnswers.csv") is False:
    print("Answer file does not exist")
    quit()

# places the two input files into datafames and sorts the interview questions by sequence number to match answers. 
# Index dosn't matter but reindexed anyways
questions_sorted = pd.read_csv("InterviewQuestions.csv").sort_values('sequencenumber', ascending = True).reset_index(drop=True)
answers = pd.read_csv("InterviewAnswers.csv")

# Generate a blank dataframe for the report
df_report = pd.DataFrame(columns = ["Question Asked","Question","Answer"])

for i in range(len(questions_sorted)):
    df_report.loc[i] = [questions_sorted.loc[i,"deletedflag"], questions_sorted.loc[i,"question"], answers.loc[i,"answer"]]

# check dataframe values in terminal
print(questions_sorted)
print(answers)
print(df_report)

# Generating Report
# Report text for first two lines and another space
report_text =[f"Conference report for {answers.loc[0, 'answer']}", f"{today}", "\n"]

# Writes the report_text line by line to csv
with open('Interview Report.csv','w', encoding='utf-8') as report:
    for line in report_text:
        report.write(line)
        report.write('\n')

# Prints the dataframe to csv with no index, header and strings and append mode.
df_report.to_csv('Interview Report.csv', encoding='utf-8', index=False, header= 'list of str', mode ='a')