def SumOddIntegers(arr,n):
    a=[]
    for i in arr:
        if i%2!=0:
            a.append(i)
    b=0
    for i in a:
        b=b+i
    return b

arr=[]
n=int(input("Enter the number of elements in the array: "))
for i in range(n):
    a=int(input("Enter the element: "))
    arr.append(a)
print(SumOddIntegers(arr,n))