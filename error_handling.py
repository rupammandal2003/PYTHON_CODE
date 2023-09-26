# a=input("Enter the number: ")
# n=input("Enter the number upto which you want the multiplication table: ")
# print(f"The multiplication table of {a} is: ")
# try:
#     for i in range(1,int(n+1)):
#         print(f"{int(a)} x {i} : {int(a)*i}")
# # except Exception as e:    # this is used to show the error
# #     print(e)
# except:
#     print("Invalid input!")
# print("Thank you")

try:
    a=int(input("Enter the number: "))
    b=[5,6,7,8]
    print(b[a])
except ValueError:
    print("Entered value is not an integer")
except IndexError:
    print("Index error")