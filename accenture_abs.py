def findcount(arr,n,dif,num):
    count=0
    for i in arr:
        if abs(i-num)<=dif:
            count+=1
    return count
arr=[int(x) for x in input().split()]
n=len(arr)
num=int(input("enter num: "))
dif=int(input("enter difference: "))
print(findcount(arr,n,dif,num))
        