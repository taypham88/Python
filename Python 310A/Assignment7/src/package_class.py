# File Contains the class definition for packages along with associated functions. 

# imported functions
import input_functions as ip
import datetime as dt
import pandas as pd
import os
import csv

# Constants
margin = dt.timedelta(days =3) # urgent date margin
date_format = '%Y-%m-%d'
air_rate_kg = 10 # air shipment cost per Kg
air_rate_vol = 20 # air shipment cost per cubic meter
truck_rate_norm = 25 # normal trucking cost
truck_rate_urg = 45 # urgent trucking cost
ocean_rate = 30 # normal ocean freight cost
weight_lim = 10 # weight limit is 10kg
volume_lim = 125 # volume limit is 125 cubic meter
big_margin = 0.8 # larger than 80% of volume or weight limit is consider big

# Package Class
class Package:
    
    def __init__(self, name : str, description : str, dangerous : bool, weight : int, volume : int , required_date, international : bool):
        
        self.id = assign_id()
        self.name = name.title()
        self.description = description
        self.dangerous = dangerous
        self.weight = weight
        self.volume = volume
        
        if self.weight >= weight_lim * big_margin or self.volume >= volume_lim * big_margin:
            self.big = True
        else:
             self.big = False
               
        self.required_date = dt.datetime.strptime(required_date, date_format).date()
        
        if self.required_date <= dt.date.today() + margin:
            self.urgent = True
        else:
            self.urgent = False 
            
        self.international = international
        
        # Below is the logic to assign route and cost. 
        # 6 possible combinations of international, urgent and dangerous. Plus considerations for big items.   
         
        # If its overweight then it can't be shipped.
        if self.weight >= weight_lim or self.volume >= volume_lim:
            self.route = "Not possible"
            self.cost = 0
         
        elif self.international == False:
            if self.urgent == True:
                if self.dangerous == True:
                    self.route = "Truck"
                    self.cost = truck_rate_urg 
                else:
                    self.route = "Air"
                    self.cost = max(air_rate_kg * self.weight, air_rate_vol * self.volume) 
            else:
                self.route = "Truck"
                self.cost = truck_rate_norm
        else:
            if self.dangerous == False:
                if self.urgent == True:                  
                    self.route = "Air"
                    self.cost = max(air_rate_kg * self.weight, air_rate_vol * self.volume)
                else:
                    self.route = "Ocean"
                    self.cost = ocean_rate
            else:
                self.route = "Ocean"
                self.cost = ocean_rate
        
    # Prints the class to csv
    def csv_print(self):
        fields=[str(self.id),str(self.name),str(self.dangerous),str(self.dangerous),str(self.weight),str(self.volume),\
            str(self.big),str(self.urgent),str(self.international),str(self.route),str(self.cost)]
        with open('Booking_Quote.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
    
    # Prints confirmation of shipping method and cost.
    def confirmation(self):
        print("--------------------------------------------------------------------------------------------------------")
        print(f"{self.name}'s package is recommended to be shipped via {self.route} freight at the cost of {self.cost}.")  
        print("--------------------------------------------------------------------------------------------------------\n")



# Assigns a unique id by adding 1 to the max. Also checks for duplicates but doesn't end program.
def assign_id():
    
    fd_list = pd.read_csv('Booking_Quote.csv', usecols= ['ID'])
    id_list = fd_list['ID'].values

    # checks a unique set of numbers against the actual number of IDs.
    if(len(set(id_list)) != len(id_list)):
        print("Warning Booking_Quote.csv has duplicate Identification numbers.")

    return max(id_list) + 1



# Checks if data exit, else it prints a message and quits
def check_path(path:str):
    
    if os.path.isfile(f'{path}') is False:
        print(f'{path} file does not exist')
        quit()



# Function to create package class and append to csv.
def create_package():
    
    name = ip.text_input("Please enter customer's name:")
    description = ip.text_input("Please enter item description.", 1, 50)
    dangerous = ip.yes_or_no("Does the package contain any dangerous items?")
    weight = ip.check_integer("What is the weight of the package?", weight_lim * 2)
    volume = ip.check_integer("What is the volume of the package?", volume_lim * 2)
    required_date = ip.date_entry("What is the required delivery date?")
    international = ip.yes_or_no("Is this an international shipment?")
        
    new_package = Package(name, description, dangerous, weight, volume, required_date, international)
    new_package.confirmation()
    
    if new_package.route == "Not possible":
        print("-------------------------------------------------------------------------------")
        print("Unfortunately this item can't be shipped due to size/weight constraints.")
        print("-------------------------------------------------------------------------------\n")
    else:
        confirm = ip.yes_or_no("Would you like to proceed with this shipment?")
        if confirm == True:
            new_package.csv_print()
        else:
            print("Package was not processed.\n")


# Function that prints pricing.             
def shipping_rates():
    print("-------------------------------------------------------------------------------")
    print("Shippings rates are as follows:\n")
    print(f"Air freight is the larger of: 10 dollars per kg or 20 dollars per cubic meter.")
    print(f"Urgent Trucking is a flat rate of 45 dollars.")
    print(f"Normal Trucking is a flat rate of 25 dollars.")
    print(f"Ocean freight is a flat rate of 30 dollars.\n")
    print(f"There is also weight limit of 10kg and volume limit of 125 cubic meters.")
    print("-------------------------------------------------------------------------------")
    