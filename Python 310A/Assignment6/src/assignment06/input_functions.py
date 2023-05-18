# File contains functions related to data entry and validation

date_format = '%Y-%m-%d' # format for date entries
import cerberus as cb
import datetime as dt

# checks if this is an integer
def check_integer(question, upperlimit = 9999, lowerlimit = 0):
    
    numb = cb.Validator({'check integer': {'min': lowerlimit, 'max': upperlimit }}) # limits validation 
    
    amount = input(f"{question} (limit {lowerlimit} - {upperlimit})")
    
    while True:
        try: 
            number = int(amount)
            if numb.validate({'check integer' : number}) == True:
                break
            else:
                print(f"Value was not within limits. between {lowerlimit} and {upperlimit}")
        except ValueError:
            print('Entry was not a number.')
    return number



# yes or no input function
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



# Date format entry
def date_entry(question):
    while True:
            
        date = input(question + '(YYYY-MM-DD):')
        try: 
            date_obj = dt.datetime.strptime(date, date_format)
            print(f"\n{date_obj.strftime(date_format)} was accepted as a date entry")
            break
        except ValueError:
            print("\nIncorrect data format, should be (YYYY-MM-DD)")
                
    return date



def text_input(question, min = 1, max = 30):
    
    char = cb.Validator({'characterlength': {'min': min, 'max': max}})
    
    flag = False
    while flag == False:

        user_input = input(question + " Between " + f"{min} to {max} character limit.")
        while char.validate({'characterlength' : len(user_input)}) == False:
            
            print(f"\nPlease enter a question between {min} and {max} characters long")
            user_input = input(question + " Between " + f"{min} to {max} character limit.")
            
        if char.validate({'characterlength' : len(user_input)}) == True:
            
            flag = yes_or_no(f"\nYou have entered '{user_input}', do you want to keep this selection?")

    print(f"'{user_input}' has been added.")
    return user_input



def ssn_entry():
    ssn_flag = False
    while ssn_flag == False:
        
        employee_ssn = input("\nPlease enter the employee's social security number. (nnn-nn-nnnn)")
        
        if (len(employee_ssn) == 11 and employee_ssn[0:3].isdigit() and employee_ssn[3] == '-' and employee_ssn[4:6].isdigit() and employee_ssn[6] == '-' and employee_ssn[7:].isdigit()):
            print(f"\n{employee_ssn} is a valid social security number.")
            
            ssn_flag = yes_or_no(f"\nYou have entered {employee_ssn}, do you want to keep this selection?")
            
        else:
            
            print(f"\n{employee_ssn} is not a valid social security number.")
            
    return employee_ssn