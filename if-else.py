# a=int(input("Enter your age: "))
# print(a)

# # conditional operators
# # >,>=,<,<=,==,!=

# print(a>18)
# print(a>=18)
# print(a<18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("You can drive")
# else:
#     print("You cannot drive")
    

# num=int(input("Enter the number you want to check: "))
# if(num<0):
#     print("number is positive")
# elif(num==0):
#     print("Number is zero")
# elif(num==999):
#     print("Number is special")
# else:
#     print("number is positive")
    
# print("I am happy now")

num=int(input("Enter the number you want to check: "))
if(num<0):
    print("number is positive")
elif(num==0):
    print("Number is zero")
else:
    if(num<=10):
        print("The number is between 0 and 10")
    elif(num>10 and num<=20):
        print("Number is between 11 and 20")
    else:
        print("The number is greater 20")