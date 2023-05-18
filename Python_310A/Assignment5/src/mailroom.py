# Tay Pham
# Nov 9, 2021 
# Assignment 5 create a program to respond to donor mail. See readme.

import inquirer as iq
import functions as f

# Initial donor list
donations =[{'Name': 'John Doe','Donations' : [5, 10, 15]},\
            {'Name': 'Jane Doe','Donations' : [11,15, 33]},\
            {'Name': 'Matt Black','Donations' : [55, 100, 150]},\
            {'Name': 'Dave Green','Donations' : [95, 10, 20]},\
            {'Name': 'Tay Pham','Donations' : [1, 1.5, 2]}]

# List in inquirer format that stores the user choices. prompt is displayed and recorded to use in the main while loop.
questions = [iq.List('choice', message = "Please select an option", choices = ['Send a Thank You', 'Create a Report', 'Mass Thank You', 'Quit'])]

# Main loop of the program. User allowed to move between selections and exits when 'Quit' selection is chosen. 
while True:
    
    answer = iq.prompt(questions) # stores user prompt selection

    if answer['choice'] == 'Send a Thank You':
        donations, donor_entry = f.new_donor(donations)
        f.generateletter(donations, donor_entry)
        print("\nLetter has been generated and placed in src/assignment05/Letters folder.")
        
    if answer['choice'] == 'Create a Report':
        f.create_report(donations)
        
    if answer['choice'] == 'Mass Thank You':
        for donor in donations:
            f.generateletter(donations, donor['Name'])
        print("\nLetters has been generated and placed in src/assignment05/Letters folder.")
        
    if answer['choice'] == 'Quit':
        break
        