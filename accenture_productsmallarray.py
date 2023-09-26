def productsmallarray(sum,arr):
    if len(arr)<2:
        return -1
    else:
        arr.sort()
        if arr[0]+arr[1]<sum:
            return arr[0]*arr[1]
        else:
            return 0

sum=int(input())
arr=[]
n=int(input("enter the number of elements in array: "))
for i in range(n):
    a=int(input("Enter the element: "))
    arr.append(a)
print(productsmallarray(sum,arr))
        
        
