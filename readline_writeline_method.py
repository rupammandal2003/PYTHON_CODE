# Readline method 

# f=open("myfile2.txt","r")
# while True:
#     line=f.readline()   # readline methid will read line by line
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     m4=line.split(",")[3]
#     print(f"The mark of {m1} in Math is {m2}")
#     print(f"The mark of {m1} in English is {m3}")
#     print(f"The mark of {m1} in Bengali is {m4}")
# f.close()

# Writeline method
# with open("myfile3.txt","w") as f:
#     line=["line1\n","line2\n","line3\n"]
#     f.writelines(line)    # writeline method will iterate from object to object

f=open("myfile4.txt","w") 
lines=["rupam","rahul","banana","cola","tea"]
for line in lines:
    line=line+ "\n"
    f.write(line)
    
