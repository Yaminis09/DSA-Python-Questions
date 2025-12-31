"""
Docstring for sum_in_loop-two

Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

data:
3
100 8
15 245
1945 54
"""


pair_number = int(input("Enter number of pairs: "))
pairs = input("Enter numbers (even count): ")

pair_list = pairs.split()
print(pair_list)

print(range(len(pair_list)))

# making elements integer
for i in range(len(pair_list)):
    pair_list[i] = int(pair_list[i])
print(pair_list)

result = []
for i in range(0, len(pair_list), 2): 
    # Finding pairs
    print("Printing pairs")
    print(pair_list[i], pair_list[i+1])
    result.append(pair_list[i] + pair_list[i+1])

print(result)