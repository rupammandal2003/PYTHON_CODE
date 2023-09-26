# FIBONACCI SERIES WITHOUT USING RECURSION

a=[0,1,1]
b=int(input("Enter the umber upto which you want to show the fibonacci series: "))
for i in range(3,b):
    a.append(a[-1]+a[-2])
# print(a) 
print("The series is",end=": ") 
for i in range(len(a)):
    print(a[i],end=",")  

from functools import reduce
print(f"\nThe sum of all the elements is: {reduce(lambda x,y:x+y,a)}")