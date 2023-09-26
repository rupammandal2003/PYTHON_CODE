numbers=[3,4,5,6,3,8,9,6]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print(f"{numbers[i]} is duplicate.")
            break
            