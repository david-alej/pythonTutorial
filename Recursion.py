# Recursion is when a define function calls itself

def factorial(n):
  if n ==1:return 1
  return n*factorial(n-1)

print(factorial(3))

# Decorators is a way to change how a function works. Decorators wrap a function, modifying its behavior.

def logtime(func):
  def wrapper():
    print('before')
    val = func()
    print('after')
  return wrapper
    

@logtime
def hello():
  print('hello')
  
hello()

# Is the same as:
print('-'*5)

def logtime(func):
  def wrapper():
    print('before')
    val = func()
    print('after')
  return wrapper
    

def hello():
  print('hello')
  
  
hello = logtime(hello)
print(hello())

# Docstrings is a description of a file, class and/or function that is denoted by three double qoutes(""" """).
# Annotations are used to specify a type of variable or return value. Python automatically ignores these annotations. Mypy wil help, idk.
#exceptions
try:
  pass
  
except:
  pass
  #catches all errors
  # if a specific error can be put with except to cathc a specific error
  
finally:
  pass
  #does something in any case
  
  
# we can raise an exception by using raise keyword
# with keyword opens a file and automatically closes after loop.
# List compressions
numbers = [1,2,3,4,5]

number_power_2 = [n**2 for n in numbers]


#Polymorphism
class Dog:
  def eat(self):
    print('Eating dog food.')
  

class Cat:
  def eat(self):
    print('Eating cat food')
    
    
animal1 = Dog()
animal2 = Cat()

print(animal1.eat, animal2.eat)

# Operator Overloading

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # represents greater than
  def __gt__(self, other):
    return True if self.age > other.age else False
  
  
roger = Dog('Roger', 8)
syd = Dog('Syd', 9)
print(roger > syd)