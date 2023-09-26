# with open("myfile.txt","r") as f:
#     print(f.read())
#     f.seek(10)
#     print(f.tell())     # tell() method indicates the current position upto the last operation ( here 10+8=18 will be shown)
#     print(f.read(8))
#     print(f.tell())     # tell() method indicates the current position upto the last operation ( here 10 will be shown)

with open("myfile5.txt","w") as f:
    f.write("hey rupam how are you?")
    f.truncate(6)
        