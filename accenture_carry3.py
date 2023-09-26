def carry(num1,num2):
    carry=0
    carry_count=0
    while num1>0 or num2>0:
        digit1=num1%10
        digit2=num2%10
        sum_digits=digit1+digit2+carry
        if sum_digits>=10:
            carry=sum_digits//10
            carry_count+=1
        else:
            carry=0
        num1//=10
        num2//=10
    return carry_count

num1=int(input())
num2=int(input())
print(carry(num1,num2))

# def NumberofCarry(num1, num2):
#     carry = 0
#     count = 0
#     while num1>0 or num2>0:
#         sum_num = num1%10 + num2%10 + carry
#         if  sum_num>=10:
#             carry = sum_num//10
#             count += 1
#         else:
#             carry = 0
#         num1 = num1//10
#         num2 = num2//10
#     print(count)       
# num1 = int(input())
# num2 = int(input())
# NumberofCarry(num1,num2)