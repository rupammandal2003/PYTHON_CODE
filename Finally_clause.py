# try:
#     s=[5,8,7,9]
#     a=int(input("Enter the index: "))
#     print(s[a])
# except:
#     print("Some error occured")
# finally:
#     print("Thak you!")   # ***Important***  ---> finally will be executed if it is inside the function also.
    
def element_print():
    try:
        s=[5,8,7,9]
        a=int(input("Enter the index: "))
        print(s[a])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("Thank you!")
    # print("Thank you!")   # It will not be executed if try and except is executed first
        
x=element_print()
print(x)