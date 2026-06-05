
"""
Input:
[10,20,5,8]

Output:
Largest = 20
Second Largest = 10
"""

def number(lista):
    first_largest = lista[0]
    second_largest = 0
    
    
    for i in range(1, len(lista)): # must run the complete length
        if lista[i] > first_largest:
            second_largest = first_largest
            print("sl")
            print(second_largest)
            first_largest = lista[i]
            print("fl1")
            print(first_largest)
        elif lista[i] > second_largest:
            second_largest = lista[i]
            print("fl2")
            print(first_largest)
            
    print(f"first_largest {first_largest}")
    print(f"second_largest {second_largest}")
    
    return

lista = [30,9,10,20,5,8]
result = number(lista)

