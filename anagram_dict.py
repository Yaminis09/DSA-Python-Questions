
def anagram(stra):
    print(stra)
    
    dicta = {}
    for word in stra:
        key = sorted(word)
        key = "".join(key)
        
        if key not in dicta:
            dicta[key] = []
        dicta[key].append(word)
    
    
            
    
    return list(dicta.values())


stra = ["eat","tea","tan","ate","nat","bat"]
result = anagram(stra)
print(result)
