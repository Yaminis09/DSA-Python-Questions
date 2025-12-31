"""
Docstring for rounding
When program deals with numbers which have fraction part we sometimes want to round such values to whole integer. We'll need this for programming some later problems (to make answers simpler, for example), so let us have the following dedicated exercise to learn this trick.

There are several pairs of numbers. For each pair you are to divide first by second and return the result, rounded to the nearest integer.

input data:
3
12 8
11 -3
400 5

answer:
2 -4 80
"""

def take_input():
    number = int(input("Enter total number of pairs: "))
    return number
def rounding():
    number = take_input()
    result = []
    for i in range(number):
        num_pair = input("Enter pair with space: ")
        num_pair = num_pair.split()
        num1 = int(num_pair[0])
        num2 = int(num_pair[1])

        quot = num1/num2  
        # print(quot)  
        if quot == int:
            result.append(quot)
        else:
            if quot >= 0:
                quot = int(quot + 0.5)
                result.append(quot)
            elif quot <0:
                quot = int(quot - 0.5)                
                result.append(quot)
    print(*(result))

rounding()       
    


