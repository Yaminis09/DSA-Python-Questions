"""
Input:
[1,2,3,5]

Output:
4

"""

def missing_one_number(lista):
    lista = sorted(lista)
    print(lista)
    first_number = lista[0]
    second_number = lista[1]
    # print(first_number)
    missing_number = []
    for idx in range(1,len(lista)):
        diff = lista[idx] - first_number
        print(f"diff : {diff}")
        print(f"num {idx}")
        if diff != idx:
            missing_number.append(diff)
            
       
        
    
    return missing_number

lista = [1,2,3,5,7]
result = missing_one_number(lista)
print(result)
