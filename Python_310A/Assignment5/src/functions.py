
# Constains all the functions used in mailroom. 
# ew_donor function, generateletter function, yes or no function and check_integer_loop function

# import os and cerberus for  use in various functions below
import os
import cerberus as cb
import pandas as df
import statistics as s


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

# This function checks if the entered value is an integer and appends entered values into a list. Will stop once the user decides to. 
def check_integer_loop(question, upperlimit, lowerlimit, list):
    
    numb = cb.Validator({'check integer': {'min': upperlimit, 'max': lowerlimit}}) # limits validation 
    
    while True:
        
        flag = False # when true a list append occurs adding a new value to the donations for the user. 
        amount = input(f"{question} (limit {upperlimit} - {lowerlimit})")
        # checks if this is an integer
        
        try: 
            number = int(amount)
            if numb.validate({'check integer' : number}) == True:
                flag = True
            else:
                print('Value was not within limits. No update was made.')
        except ValueError:
            print('Entry was not a number. No update was made.')
        # Appends the value
        
        if flag == True: 
            print('value has been updated')
            list.append(number)
            
            
        # Decides when to stop the loop    
        keep_going = yes_or_no("Would you like to enter another value?")
        if keep_going == False:
            break
        
    return list  # action to change this to integers when returned

# This function takes handles appending new users and their donations to existing dictionary. 
# Returns the entered name and dictionary for use in other functions.
# entryvalidation handles yes or no questions along with integer entries and limit checking. 
def new_donor(main_dict):
    
    blank_list =[] # used to fill new integer entries for 
    valid_entry = False # decides when a valid entry has been taken
    
    while valid_entry == False:
        initial_entry = input(f"Please enter donor name: (type 'list' to show exiting user list)").title().strip()
        
        if initial_entry == 'List':
            print('Currently we have record of the following donors:')
            for users in main_dict:
                print(users['Name'])
                
        else:
            
            for users in main_dict:
                if users['Name'] == initial_entry:
                    new_entry = yes_or_no("This is an existing donor, would you like to enter a new donation amount?")
                    if new_entry == True:
                        check_integer_loop('Please enter donation amount', 1, float('inf'), blank_list)   
                    else:
                        print('No new donation was added for this donor.')
                    valid_entry = True
                    
            if valid_entry == False:                    
                blank_list =[]
                print("This donor was not found on the list and will be added.")
                new_entry = yes_or_no("Would you like to enter a donation amount for this donor?")
                
                if new_entry == True:
                    check_integer_loop('Please enter the donation amount.', 1, float('inf'), blank_list)
                else:
                    print('No donation was added for this donor.')
                    blank_list.append(0)
                    
                main_dict.append({'Name': initial_entry, 'Donations' : blank_list})
                valid_entry = True
                
    return main_dict, initial_entry


# Generate and places the letter as a CSV into the folder Letters. located at: src/assignment05/Letters in this project.
def generateletter(main_dict, entry):
        
    lookup_info = next(item for item in main_dict if item['Name'] == entry) # looks up key pair value for name entered. 
    
    # Text for letter intro
    letter_intro = [f"Dear {entry},","\n",f"I'm writing to thank you for your generous donation of totaling {sum(lookup_info['Donations'])} dollars.", \
        "We appreciate your generosity and hope to continue this work and journey with you.","\n","Regards,","Tay Pham"]
    save_path = 'src/assignment05/Letters' # identifies the path to place the letters
    file_name = (f"{entry} Thank You Letter.csv'") # naming convention for the letters
    completeName = os.path.join(save_path, file_name)
    
    with open(completeName , 'w', encoding='utf-8') as report:
        for line in letter_intro:
            report.write(line)
            report.write('\n')


# uses pandas dataframe to generate a report on the console. Report is sorted by most donation amount          
def create_report(main_dict):
    
    report = df.DataFrame(columns =['Donor Name','Total Given', 'Num Gifts', 'Average Gift'], index = None)
    for i in range(len(main_dict)):
        report.loc[i] = [main_dict[i]['Name'],sum(main_dict[i]['Donations']), len(main_dict[i]['Donations']), round(s.mean(main_dict[i]['Donations']), 2)]
    
    
    print("The Following is a report of all donors stored:")
    print("\n")
    print(report.sort_values('Total Given', ascending = False).to_string(index = False))
    print("\n")
    return report