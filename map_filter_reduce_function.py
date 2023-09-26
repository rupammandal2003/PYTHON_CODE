# Map, Filter, Reduce these are 'higher order functions' as these take function as a input
# MAP
def square(x):
    return x**2
l=[2,5,4,8,9,69]
print(list(map(square,l)))
print(list(map(lambda x:x**2,l)))  # this is same as upper but using lambda function

# FILTER
l=[2,5,4,8,9,69]
print(list(filter(lambda x:x>4,l)))

# REDUCE
from functools import reduce   # while using reduce we have to always use  'from functools import reduce' at first
l_new=[4,5,8,6,2,5,58]
print(reduce(lambda x,y:(x+y)/2,l_new))


