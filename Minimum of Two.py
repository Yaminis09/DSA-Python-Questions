"""
Docstring for Minimum of Two

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
def take_input():
    enter_pair = input("Enter pair number: ")
    enter_pair= int(enter_pair)
    return enter_pair
def minimum_of_two():
    enter_pair  = take_input()
    result = []
    for i in range(enter_pair):
        input_pair = input("Enter pair: ")
        pair_list = input_pair.split()
        print(pair_list)
        num1 = int(pair_list[0])
        num2 = int(pair_list[1])

        if num1<num2:
            result.append(num1)
        else:
            result.append(num2)
    # print(result)
    print(*(result))

minimum_of_two()


















    

