# only for same immutable objects 'is' will be true 
# if value of both the objects are same then'==' will be true

# a=3  
# b=3
# print(a is b)  # 'is' compare the allocated memory location
# print(a==b)    # '==' compare the value 

# c=[1,5,6]
# d=[1,5,6]
# print(c is d)  
# print(c == d)

# m=(5,8,9)   # these m and n are tuple and tuples are immutable, so both output will be true
# n=(5,8,9)
# print(m is n)
# print(m == n)

a="5"
b=5
print(a is b)
print(a == b)