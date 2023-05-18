# File contains all the input handling functions used in package system.

date_format = '%Y-%m-%d' # format for date entries
import cerberus as cb
import datetime as dt

# yes or no input function
def yes_or_no(question : str):
    
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
def date_entry(question : str):
    while True:
        date = input(question + '(YYYY-MM-DD):')
        try: 
            dt.datetime.strptime(date, date_format)
            break
        except ValueError:
            print("\nIncorrect data format, should be (YYYY-MM-DD)")      
    return date



# User text input entry
def text_input(question : str, min : int = 1, max : int = 30):
    
    char = cb.Validator({'characterlength': {'min': min, 'max': max}})
    flag = False
    
    while flag == False:

        user_input = input(question + " Between " + f"{min} to {max} character limit.")
        while char.validate({'characterlength' : len(user_input)}) == False:
            
            print(f"\nPlease enter a question between {min} and {max} characters long")
            user_input = input(question + " Between " + f"{min} to {max} character limit.")
            
        if char.validate({'characterlength' : len(user_input)}) == True:
            
            flag = True

    return user_input



# Integer Entry Check
def check_integer(question : str , upperlimit : int = 9999, lowerlimit : int = 0):
    while True:
        numb = cb.Validator({'check integer': {'min': lowerlimit, 'max': upperlimit }}) # limits validation 
        amount = input(f"{question} (limit {lowerlimit} - {upperlimit})")
        try: 
            number = int(amount)
            if numb.validate({'check integer' : number}) == True:
                break
            else:
                print(f"Value was not within limits. between {lowerlimit} and {upperlimit}")
        except ValueError:
            print('Entry was not a number.')
            
    return number