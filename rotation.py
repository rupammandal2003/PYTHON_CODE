# a=int(input("Enter the number of elements: "))
# lt=[]
# for i in range(a):
#     b=int(input("Enter the element: "))
#     lt.append(b)
# c=int(input("Enter the position of the right rotation: "))
# # new_list=lt[c:len(lt)].extend(lt[0:c])
# new_list=lt[c:len(lt)]+lt[0:c]
# print(f"your list {lt} after rotating {c} right is: {new_list}")
# # print(new_list)


a=int(input("Enter the number of elements: "))
lt=[]
for i in range(a):
    b=int(input("Enter the element: "))
    lt.append(b)
c=int(input("Enter the position of the right rotation: "))
new_list=lt[-c:]+lt[-len(lt):-c]
print(f"your list {lt} after rotating {c} right is: {new_list}")
# print(new_list)