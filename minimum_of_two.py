"""
Docstring for minimum_of_two

Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.

data:
3
5 3
2 8
100 15

answer:
3 2 15

"""


number = int(input("Enter an integer: "))
number_pairs = input("Enter even pair of numbers: ")
number_pairs_list = number_pairs.split()

# Make list elements int
for num in range(len(number_pairs_list)):
    number_pairs_list[num] = int(number_pairs_list[num])
print(number_pairs_list)

# find pairs

for number in range(0, len(number_pairs_list), 2):
    # Finding pairs
    print("Printing pairs")
    print(number_pairs_list[number], number_pairs_list[number+1])
    