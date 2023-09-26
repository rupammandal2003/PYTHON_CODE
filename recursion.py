def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# p=int(input("How many numbers you want? : "))
# for i in range(p):
#     print(fibonacci(i),end=", ")

# 0 1 1 2 3 5 8 13 21 34
