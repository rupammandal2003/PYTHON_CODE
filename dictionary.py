dic={"name":"rupam","age":20,"roll no":"20ce8032","is boy?":True,586:"employee id"}
# print(dic)
print(dic["age"])
print(dic.get("name"))
# print(dic.get(586))
# print(dic.keys())
# print(dic.values())
print(dic.items())

# for key in dic.keys():
#     # print(key)
#     print(f"the value corresponding to the key {key} is {dic[key]}")

for key, value in dic.items():
    print(f"the value of key {key} is {value} ")