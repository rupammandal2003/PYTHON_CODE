# import math   # import  is used to access any variable
# print(int(math.cbrt(125)))

# import math as m    # math can be written as m by this method
# result=m.sqrt(9)*m.pi
# print(result)

# from math import sqrt,pi,cbrt   # this is used to import any particular function from the variable
# result=sqrt(25)*pi*cbrt(125)
# print(result)

# from math import *   # this is used to import all the functions from the variable
# res=sqrt(9)*pi
# print(res)


# from math import sqrt,pi,cbrt as c   # this is used to import cbrt as c 
# result=sqrt(25)*pi*c(125)
# print(result)

# import math
# print(dir(math))    # dir is used to show all the functions inside that variable
# print(type(math.nan))


import rupam as r    # this method is used to import attributes from other files --> here another file named 'rupam' is there
r.greeting()
print(r.name)

