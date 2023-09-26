def check(s1,s2):
    a=0
    for i in s1:
        for j in s2:
            if i==j:
                a+=1
    if a==len(s1) or a==len(s2):
        return "yes"
    else:
        return "no"

s1=input()
s2=input()
print(check(s1,s2))