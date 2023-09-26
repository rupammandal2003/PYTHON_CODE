# def func(a=1,b=3,c=5):
#     print("The average of these numbers is ",(a+b+c)/3)

# # func(10,15)    # if any value among a,b,c is not taken as input then the interpretor will consider the default value
# # func()   # if no value is taken as input, then the python interpretor will consider the default values which are inside the function

# func(2,5,9)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # return sum/len(numbers)
    print("The sum of these ",len(numbers)," numbers is ",sum/len(numbers))
    # return 7    # if two or more return values are taken then only the first value will be returned

# c=average(4,5,8,9,4)
# print(c)
# print(type(c))

average(8,9,6,4,7)