s1={4,5,7,8,9,4}
s2={2,4,25,7,58}
# s3=s1.union(s2)
# print(s3)
# s1.update(s2)
# print(s1)

# s4=s1.intersection(s2)
# print(s4)
# print(s1)
# s1.intersection_update(s2)
# print(s1)

# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)

# print(s1.isdisjoint(s2))

cities={"delhi","mumbai","chennai","bengaluru"}
cities1={"delhi","bengaluru","kolkata"}
# print(cities.issuperset(cities1))
# print(cities1.issubset(cities))

# cities.add("khatra")
# print(cities)

# cities.update(cities1)
# print(cities)

# item=cities.pop()
# print(item)

# cities.remove("jhansi")  # remove will through an error if the element is not found 
cities.discard("jhansi")   # discard will not through an error, it will pass the code to the next operation

# del cities   # 'del' will delete the entire set
# print(cities)

# cities.clear()   # 'clear()' will delete all the elements in the set but will not delete the set and as a output we will get an empty set
# print(cities)

for city in cities:
    if city=="khatra":
        print("yes it's present")
    else:
        print("no")

