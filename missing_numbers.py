"""
Input:
[1,2,3,5]

Output:
4

"""

def missing_numbers(lista):
    lista = sorted(lista)
   
    
    missing_number = []
    for num in range(len(lista)-1):
        current_number = lista[num]
        next_number = lista[num+1]
        
        if next_number - current_number >1:
            for miss in range(current_number +1, next_number):
                missing_number.append(miss)
       
        
    
    return missing_number

lista = [1,2,3,5,7,14]
result = missing_numbers(lista)
print(result)
