def largeSmallSum(arr):
    list=[]
    for i in arr:
        list.append(int(i))
        odd=[]
    for i in range(0,len(list),2):
        odd.append(list[i])
    odd.sort()
    second_large_odd=odd[-2]
    even=[]
    for i in range(1,len(list),2):
        even.append(list[i])
    even.sort()
    second_large_even=even[-2]
    if len(list)==0:
        return 0
    elif len(list)<=3:
        return 0
    else:
        return second_large_even+second_large_odd    

print(largeSmallSum("321754"))

