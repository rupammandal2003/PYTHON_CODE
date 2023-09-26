def cube(x):
    return x**3

cube1=lambda x:x**3   # lambda function works as a short function which takes input and return the output( lambda arguments:expression)
print(cube(5))
print(cube1(3))

avg=lambda a,b,c:(a+b+c)/3   # it takes multiple input also
print(avg(6,8,9))

def sum(fx,x):   # we can pass a function as an argument inside the function also
    return 6+fx(x)

print(sum(cube,3))
print(sum(lambda x:x**0.5,25)) # for a short function lambda function is used