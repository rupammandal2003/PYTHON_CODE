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
        m=x
        n=y
        # a=a[x-m:x+1]
    elif x==y:
        m=x
    else:
        m=y
        n=x
        # b=b[y-m:y+1]
    if x==y:
        while m>=0:
            c=a[m]+b[m]
            if c>=10:
                if c>10:
                    k=c-10
                else:
                    k=1
                sum_of_Carry+=1
                if m>=1:
                    b[m-1]=b[m-1]+k
            m=m-1
    else:
        count=0
        while m>=0:
            while n>=0:
                if n>=1:
                    c=a[m]+b[n]
                    if c>=10:
                        if c>10:
                            k=c-10
                        else:
                            k=1
                        sum_of_Carry+=1
                        
                        b[n-1]=b[n-1]+k
                    m=m-1
                    n=n-1
                else:
                    c=a[m]+b[n]
                    if c>=10:
                        if c>10:
                             k=c-10
                        else:
                            k=1
                        count+=1
                        sum_of_Carry+=1
                    m=m-1
                    n=n-1
            if count==1:
                a[m]=a[m]+1
                if a[m]>10:
                    sum_of_Carry+=1
                    m=m-1
                    
            # else:
            #     continue
                    
            # m=m-1
    return sum_of_Carry
        
num1=int(input())
num2=int(input())
print(carryof(num1,num2))