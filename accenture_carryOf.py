def carryof(num1,num2):
    sum_of_Carry=0
    a=[]
    b=[]
    num1=str(num1)
    for i in num1:
        a.append(int(i))    
    num2=str(num2)
    for i in num2:
        b.append(int(i))
    x=len(a)-1
    y=len(b)-1
    if x>y:
        m=y
        a=a[x-m:x+1]
    elif x==y:
        m=x
    else:
        m=x
        b=b[y-m:y+1]
    
    while m>=0:
        c=a[m]+b[m]
        if c>=10:
            n=c-10
            sum_of_Carry+=1
            if m>=1:
                b[m-1]=b[m-1]+n
        # else:
        #     continue
                
        m=m-1
    return sum_of_Carry
        
num1=int(input())
num2=int(input())
print(carryof(num1,num2))

# def Numberofcarry(num1, num2):
#     carry_count = 0
#     carry = 0
    
#     while num1 > 0 or num2 > 0:
#         digit1 = num1 % 10
#         digit2 = num2 % 10
        
#         sum_digits = digit1 + digit2 + carry
#         carry = sum_digits // 10
        
#         if carry > 0:
#             carry_count += 1
        
#         num1 //= 10
#         num2 //= 10
    
#     return carry_count

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# result = Numberofcarry(num1, num2)
# print("Output:",result)