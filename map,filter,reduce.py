# map(), filter(), list()
# map() is a global function used to run another function in a iterable object.

numbers = [1,2,3]

def double(a):
    return a * 2
  
# OR double = lambda a: a * 2
result = map(double, numbers)

# The result is a amp object tha is an iterable, to prints its contents we covert it to a list
print(list(result))


# filter() takes a iterable object and returns an filter object, which is iterable, without objects that do not fit condition
def is_even(n):
  return n % 2 == 0

result = filter(is_even, numbers)

print(list(result))


# reduce() is used to calculate a value out of an iterable object
from functools import reduce

expenses = [
  ('Dinner', 80),
  ('Car repair', 120)
] 

sum = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum)