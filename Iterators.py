# Iterator is an object that contains a countable number of values. It can also be iterted upon, meaning that you can tranverse through all the values. Iterators consists of methods __iter__() and __next__().
# Iterable objects, like lists, strings, tuples, and sets, which can be in iterator form.
#An exampleof having a iterable object in a iretator form is
mytuple = ('apple', 'bannana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#OR we cna say
for x in mytuple:
  print(x)
  
#We can do this to a string to
mystr = 'apple'

for x in mystr:
  print(x)
  
  
# TO create an objet/class as an iterator you have to implement the methods __iter__() and __next__(), like so:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  
  def __next__(self):
    #We can add a terminating condition to raise an error if the itertin is done specified number of times by adding this if/else staement.
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
  
    else:
      raise StopIteration


for x in MyNumbers():
  print(x)
