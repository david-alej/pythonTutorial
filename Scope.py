# Scope is the region where a variable is availble inside
# There is local scope and global scope. AN example of a local scope is a vairable inside a function, it can only be used inside the function. 
x = 50
def myfunc():
  x= 300
  print(x)
  # if there is a function inside this functin we can still use vairable for the sub-function
myfunc()
print(x)
#A vairable created in the main bod of Python code is a global variable and belongs to the global scope. GLobal scope are aviliable within any scope, global or local
x = 150

def myfunc():
  print(x)
  
  
myfunc()
print(x)


# If the same variable is used in a global and local scope they will be treated as two seperate vairable, the one that was in the main body will be availible anywhere but the function that the same variable was reused. The reused variable used in the function while only be avialable insid ethat function

# One can use the global keyword to either create or change a global scope variable

def myfunc():
  global x
  x = 299


myfunc() 
print(x) 

#or

y = 250

def myfunc():
  global y
  y = 233
  

myfunc()
print(y)