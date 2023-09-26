def list_to_string(s):
    string=" "
    for j  in s:
        string=string+j
    print(string)
        
a=input("Enter your message --> ")
b=list(a)
copy_b_for_space_removal=b.copy()
blank_space=[index for index,ele in enumerate(b) if ele==' ']
print(blank_space)
for i in copy_b_for_space_removal:
    if i==' ':
        copy_b_for_space_removal.remove(i)
        copy_b_for_space_removal=copy_b_for_space_removal
i=a.split()
k=[]
for c in i:
    c=list(c)
    if len(c)<3:
        c.reverse()
        k.extend(c)
        
        # list_to_string(c)
    else:
        
        copy_c=c.copy()
        del copy_c[0:2]
        del c[2:len(c)]
        copy_c.extend(c)
        k.extend(copy_c)
        
        # list_to_string(copy_c)

list_to_string(k)
