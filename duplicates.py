

"""
[1,3,2,2,3,4,4]

Output:
[1,2,3,4]
"""
# sort the array
# count the element
def remove_duplicates(lista):
    # lista = set(lista)
    # return list(lista)
    dicta = {}
    for i in lista:
        if i in dicta:
            dicta[i]+=1
            
        else:
            dicta[i] = 1
    return list(dicta.keys()) 
    
def get_duplicates(lista):
    dictb = {}
    for i in lista:
        if i in dictb:
            dictb[i]+=1
            
        else:
            dictb[i] = 1
    print(dictb)
   
            
    result = []
    for key, value in dictb.items():
        if value > 1:
            result.append(key)
    
    return result
    
    
    
lista = [1,3,2,2,3,4,4,6,6,6,6,6,66,]
resultsa = remove_duplicates(lista)
print(resultsa)
resultsb = get_duplicates(lista)
print(resultsb)
