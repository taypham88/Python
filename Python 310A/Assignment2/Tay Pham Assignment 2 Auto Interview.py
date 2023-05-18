# Tay Pham Assignment 2 10/19/2021
# Program will ask 2 sets of questions to each guest, stores the data and prints it for the guest to confrim. 

# List of inital Questons
intro_questions = ["What is your name?",\
    "What is your conference ID?",\
    "Which organization do you represent?",\
    "What is your email address?",\
    "State any food preferences?",]

# List of seminar choices
seminar_choices = ["Python for beginners",\
    "Database development with Python",\
    "Python for data science",\
    "Advanced Python for application developers"]

# List of answers to intial questions
intro_answers =["Your name is", "Your conference ID is", \
    "The organization you are representing is", "Your email address is", \
    "Your food preference is"]

# Prints Welcom message
print("Welcome to the Python Seminar")

# Sets up 2 blank list to store answers
intro_inputs =[]
seminar_inputs =[]

# Set up counters for while loops
b = 0
c = 0

# For loop to collect intial questions
# will cycle through intro_question list and collect inputs and striping out white space. 
for x in range(len(intro_questions)):
    intro_inputs.append(input(intro_questions[x]).strip())


# For loop to collect seminar qeustions
# will cycle through seminar choice questions and assign a boolean base on the text input. 
# Non y or n inputs will be assumed a No answer.
for x in range(len(seminar_choices)):
    seminar_ans = input(f"{seminar_choices[x]} (Please enter Y or N)")
    if seminar_ans.strip().upper() == "Y":
        seminar_inputs.append(True)
    elif seminar_ans.strip().upper() == "N":
        seminar_inputs.append(False)
    else:
        print("invalid Input, Choice Taken as No")
        seminar_inputs.append(False)


# Prints the collected answers to intro questions back to the user.
# Uses intro_answers text list combined with collected inputs
while b < len(intro_questions):
    print(f"{intro_answers[b]} {intro_inputs[b]}")
    b = b + 1


# Prints the response to seminar choices base on boolean stored in seminar_inputs 
while c < len(seminar_choices):
    if seminar_inputs[c] == True:
        print(f"You would like to take {seminar_choices[c]}")
    else:
        print(f"You would not like to take {seminar_choices[c]}")
    c = c + 1


# departing message
print("If there is any error in this information please see a representative inside")
print("Thank you and have a nice day!")