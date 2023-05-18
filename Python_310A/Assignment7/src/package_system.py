# Tay Pham
# Booking System Homework
# see readme for detailed instructions
# This is the main file where everything is ran

import package_class as pc

# checks if required csv is reachable
pc.check_path('Booking_Quote.csv')

while True:
    
    # Prints Menu for selection
    print("-------------------------------------------------------------------------------")
    print("Welcome to the package handling system. Please choose from the following menu:\n")
    print("1: Create a new package entry.\n")
    print("2: Show shipping rates.\n")
    print("q: exit program \n")
    
    user_input = input("Please enter a selection:")

    if user_input.lower() == "q" or user_input.lower() == "quit":
        break
        
    elif user_input == "1":
        pc.create_package()
        
    elif user_input == "2":
        pc.shipping_rates()
    
    else:
        print("Invalid input, please try again.")


