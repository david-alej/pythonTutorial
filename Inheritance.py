# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class - the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

 
  def printname(self):
    print(self.firstname, self.lastname)
    

# Child class
# class Student(Person):
#   pass


#You can add the __innit__ function that is called automatically everyt ime the class is being used to create a new object. The child class will no longer inherit parent's __innit__(), as it ovrrideds inheritance of parents innit.
#class Student(Person):
#  def __innit__(self, fname, lname):
#    pass
    
    
#To keep inheritance of parent's innit function we can write
#class Student(Person):
#  def __innit__(self, fname, lname):
#    Person.__innit__(self, fname, lname)
    
    
# We can also use the super() function in the chaild class to inherit all the methods and propeties from its parent
#class Student(Person):
#  def __innit__(self, fname, lname):
#    super().__innit__(fname, lname)
    
    
# We can also add propeties to child class, using the same syntax as used in the Parent class used above
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__( fname, lname)
    self.graduationyear = year
    
    
  #We can also add methods the same as Parent's class
  def welcome(self):
     return print(f'Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}')


x = Student( 'David', 'Alejandro', 2022)
print(x.welcome())
    


