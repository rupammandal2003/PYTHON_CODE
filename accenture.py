r=int(input())
unit=int(input())
arr=[]
n=int(input("Enter the number of members: "))
for i in range(n):
    m=input("Enter the element: ")
    arr.append(m)
# print(arr)
sum_of_all_ele=0
for i in range(len(arr)):
    sum_of_all_ele=sum_of_all_ele+int(arr[i])
# print(sum_of_all_ele)
sum=0
sum_ele=0
for j in range(len(arr)):
    sum=sum+int(arr[j])
    sum_ele+=1
    if sum>=r*unit:
        break
if n==0:
    print(-1)
elif r*unit>sum_of_all_ele:
    print(0)
else:
    print(sum_ele)
