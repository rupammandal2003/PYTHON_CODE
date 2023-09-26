def differenceofSum(m,n):
    sum_not_m=0
    sum_m=0
    for i in range(1,n+1):
        if i%m!=0:
            sum_not_m+=i
        if i%m==0:
            sum_m+=i
    return sum_not_m-sum_m

print(differenceofSum(6,30))