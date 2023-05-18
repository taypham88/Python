# Tay Pham
# Human Resource System
# See readme for detailed instruction. 

import os
import pandas as pd
import functions as f
import inquirer as iq

# Checks if data exit, else it prints a message and quits    
if os.path.isfile("HR_Data.csv") is False:
	print("HR_Data.csv file does not exist")
	quit()

# Import HR data as a pandas dataframe and sort by ID. 
raw_hr_data =[]
raw_hr_data = pd.read_csv("HR_Data.csv").sort_values('ID', ascending = True).reset_index(drop=True)

# Convert Dataframe to List of Employee Class 
hr_data = [(f.Employee(row.Name, row.ID, row.Address, row.SSN, row.DOB, row.Job_Title, row.Start_Date, row.End_Date)) \
    for index, row in raw_hr_data.iterrows()]

# Check that all employee IDs are unique. Will print a message and exit. 
lid = [] # list to collect all employee IDs. 
for employee in hr_data:
    lid.append(employee.id)
    
# checks a unique set of numbers against the actual number of IDs.
if(len(set(lid)) != len(lid)):
    print("HR_Data.csv has duplicate employee Identification numbers.")
    quit()

# List in inquirer format that stores the user choices. prompt is displayed and recorded to use in the main while loop.
print("\nWelcome to the Human Resource Employee Database Management System.")
questions = [iq.List('choice', message = "Please select an option", \
    choices = ['New Employee Entry', 'Edit Employee info', 'Create Turnover Report', 'Create Active Employee Report',\
        'Display Upcoming Employee Reviews', 'Quit'])]

while True:
    answer = iq.prompt(questions) # stores user prompt selection
    
    if answer['choice'] == 'New Employee Entry':
    	hr_data = f.employee_entry(hr_data)
    
    if answer['choice'] == 'Edit Employee info':
        f.active_employees(hr_data, all = True)
        hr_data = f.change_info(hr_data)
        
    if answer['choice'] == 'Create Turnover Report':
    	f.employees_turnover(hr_data)
        
    if answer['choice'] == 'Create Active Employee Report':
        f.active_employees(hr_data)
        
    if answer['choice'] == 'Display Upcoming Employee Reviews':
    	f.employees_review(hr_data)
     
    if answer['choice'] == 'Quit':
        break
