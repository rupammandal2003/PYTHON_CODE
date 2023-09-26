def virus_attack(numbers, n):
    final_numbers = []
    for num in numbers:
        binary_num = bin(num)[2:]  # Convert the decimal number to binary
        eaten_digits = min(n, len(binary_num))  # Calculate how many digits will be eaten
        result_binary = '0' * eaten_digits + binary_num[:-eaten_digits]  # Create the final binary number
        final_numbers.append(int(result_binary, 2))  # Convert binary back to decimal and add to the result list
    return final_numbers

n=int(input())
a=input()
initial_numbers = [int(i) for i in a.split()]
spike_count = int(input())
final_result = virus_attack(initial_numbers, spike_count)
# print(final_result)
for i in final_result:
    print(i,end=" ")