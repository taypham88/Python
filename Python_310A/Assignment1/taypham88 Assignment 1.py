# Tay Pham Python 310A Assignment 1 10/12/2021
# Basics
# 1. Assign a string, integer and float value to variables called respectively mystring, myinteger and myfloat.

mystring = "pie" # string
myinteger = 10 # integer
myfloat= 3.14 # float

# Check work
print("Problem 1 Check")
print(f"mystring variable type is {type(mystring)}")
print(f"myinteger variable type is {type(myinteger)}")
print(f"myfloat variable type is {type(myfloat)}")

# 2. Write code to add two int variables, storing the result in a third variable. 
# Check that the third variable has the correct value.

int_var1 = 1 # First integer
int_var2 = 2 # Second integer
int_var3 = int_var1 + int_var2 # sum of integer

# Check work
print("Problem 2 Check")
print(f"Problem 2 value is {int_var3} and type as {type(int_var3)}") 

# 3. Write code to add two float variables, storing the result in a third variable. 
# Check that the third variable has the correct value.

float_var1 = 6.9 # First float
float_var2 = 3.1 # Second flaot
float_var3 = float_var1 + float_var2 # sum of float

# Check work
print("Problem 3 Check")
print(f"Problem 3 value is {float_var3} with the type as {type(float_var3)}") 
print(f"Problem 3 rounded value is {round(float_var3)}") 

# 4. Write code to add two str variables, storing the result in a third variable. 
# Check that the third variable has the correct value.

string_var1 = "Power " # First string
string_var2 = "Rangers" # Second string
string_var3 = string_var1 + string_var2 # sum of string

# Check work
print("Problem 4 Check")
print(f"Problem 4 value is {string_var3} and a type as {type(string_var3)}") 

# 5. Write code to add an int and a float variable, storing the result in a third variable. 
# Check that the third variable has the correct value.

int_item = 6 # First float
float_item = 3.14 # Second flaot
sum_item = int_item + float_item # sum of float

# Check work
print("Problem 5 Check")
print(f"Problem 5 value is {sum_item} with the type as {type(sum_item)}") 

# 6. Write code to add an int variable and a str variable. What happens? Why? Record your answer in a comment.

# Below is the code for problem 6 commented out. 
# The response you get back is "TypeError: can only concatenate str (not "int") to str" you can not add a string and an integer.
# You will need to convert the integer to a string first. 
# string_add_integer = string_var1 + int_var1

# Try these tasks problems

# 1. Assign a string, integer and float value to variables called respectively mystring, myinteger and myfloat. 
# Write code to prove that the values really are a str, int and float.
# Answer: see part one of basic problems.

# 2. Can you find a way to add an int value to a str? Check the resulting value.

string_add_integer = string_var1 + str(int_var1)
print(f"Additional tasks problem 2's value is {string_add_integer} \
with the type as {type(string_add_integer)}")

# 3. Multiply 5 by 7.654321 and round to 3 decimal places. Check the resulting value.

problem_3answer = round(5 * 7.654321, 3)
print(f"Additional tasks problem 3's value is {problem_3answer}")

# 4. Use the input function to display a message that says “Enter your name” and places the result in a variable called myname. 
# Check the resulting value.

myname = input("Enter your name: ")
print("Check additional tasks problem 4")
print(f"The name entered is {myname}")

# 5. Use the input function to display a message that says “Enter your favorite number” and places the result in a variable called favorite_number. 
# Check the resulting value. And check its type. Any surprises?

favorite_number = input("Enter your favorite number: ")
print("Check additional tasks problem 5")
print(f"Number entered is {favorite_number} with the type as \
{type(favorite_number)}")
# Inputs are stored as strings which is a surprise.

# 6. Now, use input to display a message asking for a number. Then another message asking for a second number. 
# Then print the sum of the two numbers. Check the resulting values. 
# Any surprises? For 4 and 5 the program should display 9. If it doesn’t investigate and fix the error.

first_number = input("Enter a number: ")
second_number = input("Enter another number: ")
sum_ofnumbers = int(first_number) + int(second_number)
print(f"Additional tasks Problem 6's number sum is {sum_ofnumbers} \
with a type of {type(sum_ofnumbers)}")

# if you do not use the int() function to convert the inputs, they will stay as strings and the number values will add like a string
# For example 5 and 4 will be 54 rather than 9 as the problem wanted.