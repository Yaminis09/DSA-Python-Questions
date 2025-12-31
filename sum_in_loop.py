"""
Input data has the following format:

first line contains N - amount of values to sum;
second line contains N values themselves.
Answer should contain a single value - the sum of N values.
"""

enter_total_number = int(input("Enter total number: "))
enter_all_the_numbers = input("Enter the individual number with space( number same as total number): ") # gives you a string
print(type(enter_all_the_numbers))
number_list = enter_all_the_numbers.split() # makes it a list
print(type(number_list))

count = 0
for num in number_list:
    count +=int(num) # adds like 0 +first number. gives solution. now adds solution with the second element of the list. 
    

print(count)


