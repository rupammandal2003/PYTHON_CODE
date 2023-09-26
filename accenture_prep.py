a=int(input("Enter the size of the array: "))
b=[]
x=1
for i in range(a):
    c=int(input(f"Enter the {x} element: "))
    b.append(c)
    x+=1
odd=b[0:len(b):2]
odd.sort(reverse=True)
# print(odd)
even=b[1:len(b):2]
even.sort(reverse=True)
# print(even)
def sum_even_odd(lst1,lst2):
    a=0
    b=0
    m=lst1[0]
    for i in lst1:
        if i<m:
            a=a+i
            break
    n=lst2[0]
    for j in lst2:
        if j<n:
            b=b+j
            break
    return a+b
print(sum_even_odd(even,odd))