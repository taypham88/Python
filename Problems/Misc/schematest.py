from cerberus import Validator

schema = {'characterlength': {'min': 10, 'max': 30}}
v = Validator(schema)

string1 = 'i am more than 10 characters'
string2 = 'small'
pi =[]
try:
   pi = v.validate({'characterlength': len(string1)}) != True
   print(v.validate({'characterlength': len(string1)}))
except:
    print('not within range') 

try:
   pi = v.validate({'characterlength': len(string2)}) != True
   print(v.validate({'characterlength': len(string2)}))
except:
    print('not within range') 
