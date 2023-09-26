# dir={"jan":2200,"feb":2350}
dir={}
a=int(input("Enter the number of months: "))
for i in range(a):
    month=input("Enter the month: ")
    expense=input(f"enter the expense in the month {month}: ")
    dir[month]=expense
print(dir)

def diff_in_months(dir):
    month1=input("Enter the month: ")
    month2=input("Enter the month: ")
    print(f"The difference in expenses between {month1} and {month2} is: {dir[month1]-dir[month2]}")
    
diff_in_months(dir)