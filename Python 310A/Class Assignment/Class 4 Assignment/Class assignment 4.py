# Class assignment 4
# Use Cerberus to do the following:
# Name, String, 10-30 characters
# Age, integer, must be between 18 and 65
# SSN, String, must be nnn-nn-nnnn
# Phone number, String, must be nnn.nnn.nnnn

from cerberus import Validator

Name = 'Tay Pham The Long Name'
Age = 33
SSN = '555-55-5555'
Phone_number = '555.555.5555'

name_schema = {'name': {'minlength': 10, 'maxlength': 30}}
print(len(Name))
v = Validator(name_schema)
print(v.validate(Name))