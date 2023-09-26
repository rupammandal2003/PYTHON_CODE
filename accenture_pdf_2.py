def inversioncount(arr,n):
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
    return count

arr=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    a=int(input("Enter the value: "))
    arr.append(a)
print(inversioncount(arr,n))