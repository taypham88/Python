# Functions File for hr_system

import datetime as dt
import pandas as pd
import inquirer as iq
import input_functions as ip

# Format for which all dates will be recorded.
date_format = '%Y-%m-%d'

class Employee:
    
    def __init__(self, name, id, address, ssn, dob, job_title, start_date, end_date = 'None'):
        self.name = name.title()
        self.id = int(id)
        self.address = address
        self.ssn = ssn
        self.dob = dt.datetime.strptime(dob, date_format).date()
        self.job_title = job_title.title()
        self.start_date = dt.datetime.strptime(start_date, date_format).date()
        if end_date == 'None':
            self.end_date = 'None'
        else:
            self.end_date = dt.datetime.strptime(end_date, date_format).date() 

    def to_dict(self):
        return {
            'Name': self.name,
            'ID': self.id,
            'Address': self.address,
            'SSN': self.ssn,
            'DOB': self.dob,
            'Job_Title': self.job_title,
            'Start_Date': self.start_date,
            'End_Date': self.end_date}



def write_csv(data):
    # Prints new csv database with added employee. First clears it then rebuilds the csv.
    f = open('HR_Data.csv', "w")
    f.truncate()
    f.close()
    pd.DataFrame.from_records([s.to_dict() for s in data]).to_csv('HR_Data.csv', encoding='utf-8', index=False, header= 'list of str', mode ='a')
  


# Function prints a report for current active employees
def active_employees(data, all = False):
    # List used for appending active employee info
    lname = []
    lid = []
    
    # Checks for all instances of having no end date
    for employee in data:
        if all == False:
            if employee.end_date == "None":
                lname.append(employee.name)
                lid.append(employee.id)
        if all == True:
                lname.append(employee.name)
                lid.append(employee.id)            
            
    # Constructs a dictionary then converts to pandas dataframe for report.               
    dic = {'Employee ID' : lid, 'Employee Name' : lname}
    active_employee_report = pd.DataFrame.from_dict(dic, orient ='columns')
    print("\nThe Following employees are currently working at the company:")
    print(active_employee_report.to_string(index = False))
    
    
    
# Function prints a report for employee who have left in the last month
def employees_turnover(data):
    # List used for appending active employee info
    lname = []
    lid = []
    lend_date = []
    
    # date used to check for 1 months(30 day range)
    margin = dt.timedelta(days = 30)
    today = dt.date.today()
    
    # Checks for all instances of having no end date and then dates that fall within range of a month from today.
    for employee in data:
        if employee.end_date != "None":
            if employee.end_date >= today - margin:
                lname.append(employee.name)
                lid.append(employee.id)
                lend_date.append(employee.end_date)
    
    # Constructs a dictionary then converts to pandas dataframe for report.        
    dic = {'Employee ID' : lid, 'Employee Name' : lname, 'Employee Last day' : lend_date}
    employee_turnover_report = pd.DataFrame.from_dict(dic, orient ='columns')
    print("\nThe Following employees left the company in the last month:")
    print(employee_turnover_report.to_string(index = False))
    
    
    
# Function prints a report for employees with start months and days within 90 days of today's date   
def employees_review(data):
    # list used to append info for report
    lname = []
    lid = []
    lcounter = []
    lstartdate = []
    
    # dates used in calcs
    margin = dt.timedelta(days = 90)
    today = dt.date.today()
    this_year = dt.date.today().strftime("%Y")
    
    for employee in data:
        d1 = employee.start_date # employee start date
        d2 = dt.date(int(this_year), d1.month, d1.day) # employee start date with this year 
        d3 = dt.date(int(this_year) + 1, d1.month, d1.day) # employee start date with next year 
        
        if employee.start_date.strftime("%Y") != this_year:
            if today <= d2 <= today + margin or today <= d3 <=  today + margin:
                lname.append(employee.name)
                lid.append(employee.id)
                if abs(d2 - today) <= margin:
                    lcounter.append(d2-today)
                else:
                    lcounter.append(d3 - today)
                lstartdate.append(employee.start_date)
    
    # Constructs a dictionary then converts to pandas dataframe for report.        
    dic = {'Employee ID' : lid, 'Employee Name' : lname, 'Days until review': lcounter,'Employee Start Date' : lstartdate}
    employee_review_report = pd.DataFrame.from_dict(dic, orient ='columns')
    print("\nThe Following employees have reviews within 90 days:")
    print(employee_review_report.to_string(index = False))



# Function to process new employee entries
def employee_entry(data):
    print("\nYou wish to add a new employee to the database.")
    
    # Name entry for new employee. Set limit to between 5 and 30 characters.
    employee_name = ip.text_input("\nPlease enter the employee's name you wish to add.", 5, 30)

    # Generates a new id by adding one to the largest ID. 
    lid=[]
    for employees in data:
        
        lid.append(employees.id)
        
    new_id = max(lid) + 1
    print(f"\nThe employee ID number {new_id} has been autogenerated for {employee_name}.")
    
    # Text address entry for new employee address. Set limit to between 10 and 50 characters.
    employee_address = ip.text_input("\nPlease enter the employee's address.", 10, 50)

    # Social Security number input. Checks for formatting. 
    employee_ssn = ip.ssn_entry()
    print(f"\n{employee_ssn} has been added.") 
    
    # Date entry for employee date of birth
    employee_dob = ip.date_entry("Please enter a date of birth for employee.")
    
    # Allows employee job title entry. Set limit to between 5 and 20 characters.
    employee_jobtitle = ip.text_input("Please enter an employee job title.", 5, 20)

    # Date entry for employee start date
    employee_startdate = ip.date_entry("Please enter a start date for employee.")
    
    # add new employee to exiting datastructure.
    data.append(Employee(employee_name, new_id, employee_address, employee_ssn, employee_dob, employee_jobtitle, employee_startdate))
    
    write_csv(data) # updates the csv file 
    
    return data



def change_info(data):
    
    flag = True
    while flag == True:
        
        employee_id = ip.check_integer("Please enter employee ID. Enter 0 to exit.")
        
        if employee_id == 0:
            break
        
        for employee in data:
            if employee.id == employee_id:
                print(f'You have entered the {employee.name}.')
                affirm = ip.yes_or_no(f"You have entered {employee.name}'s ID. Is this correct?")
                if affirm == True:
                    employee = question_list(employee)
                    flag = False
                else:
                    continue
                
        if flag == True:
            print("Please try again")
            
    write_csv(data) # updates the csv file 
    return data



def question_list(employee):
    
    questions = [iq.List('choice', message = 'Which item would you like to edit?', \
        choices = ['Name', 'Address', 'SSN', 'DOB', 'Job_Title', 'Start_Date', 'End_Date', 'Quit'])]
    
    answer = iq.prompt(questions)
    
    if answer['choice'] == 'Name':
        employee.name = ip.text_input("\nPlease enter the employee's name you wish to add.", 5, 30)
        print(f"\n Employee Name has been updated to {employee.name}.") 
    
    if answer['choice'] == 'Address':
        employee.address = ip.text_input("\nPlease enter the employee's address.", 10, 50)
        print(f"\n{employee.name}'s address has been updated.") 
     
    if answer['choice'] == 'SSN':
        employee_ssn = ip.ssn_entry()
        employee.ssn = employee_ssn        
        print(f"\n{employee.name}'s SSN has been updated.")  

    if answer['choice'] == 'DOB':
        employee.dob = ip.date_entry("Please enter a date of birth for employee.")
        print(f"\n{employee.name}'s DOB has been updated.") 

    if answer['choice'] == 'Job_Title':
        employee.job_title = ip.text_input("Please enter an employee job title.", 5, 20)
        print(f"\n{employee.name}'s Job Title has been updated.") 
        
    if answer['choice'] == 'Start_Date':
        employee.start_date = ip.date_entry("Please enter a start date for employee.")
        print(f"\n{employee.name}'s Start Date has been updated.") 
        
    if answer['choice'] == 'End_Date':
        employee.end_date = ip.date_entry("Please enter a start date for employee.")
        print(f"\n{employee.name}'s End Date has been updated.") 
    
    if answer['choice'] == 'Quit':
        print('No edits made')
    
    return employee