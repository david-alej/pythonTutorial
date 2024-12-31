# You can import built-in modules in Python. Modules are files containing funcitons and vairables of all types (arrays, dictionaries, objects etc). One can use the dir() function to list all the function names in a module.
# One can import modules by :
# import [name of module] 
# Or:
# from [name of module] import [specific function]
# Or we can also rename what we are import like:
# from [name of module] import [specific function] as [name function or module]
# using as keyword
import platform as pf

x = pf.system()
print(x, dir(pf))

# Some module showcased are platform, math, Dates,JSON
#JSON is a syntax storing and exchanging data, which is text written with JavaScript notation
# We can convert python to JSON using this module, we can even customize the s=results
import json

x = {
  'name': 'John',
  'age': 30,
  'married': True,
  'divorced': False,
  'children': ('Ann', 'Billy'),
  'pets': None,
  'Cars': [
    {'model': 'BMW 230', 'mpg': 27.5},
    {'model': 'Ford Edge', 'mpg': 24.1}
  ]
  
}


print(json.dumps(x, indent =4, separators = ('.', '='), sort_keys = True))

#RegEx or  Regular Expression is a sequence of chracter sthat forms a search pattern( import re).
# A package contains all the files you need for a module. Modules are python code libraries you can includ in your project.
# You can use input() function for python to alow for user input.
#The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when theer is no error
# Finally block lets you execute code, regardles fo the result of the try- and except blocks
# you can use the raise keyword to raise an exception using an if staement
x = -1

# if x<0:
#   raise Exception('Sorry, no numbers below zero')

#OR
x = 'hello'

if not type(x) is int:
  raise TypeError('Only integers are allowed')