

def dict_change(dicta):
    
    print(dicta)
    
    new_dict = {}
    
    for key, value in dicta.items():
        print(f"key: {key}")
        print(f"value {value}")
        if value not in new_dict:
            
            new_dict[value] =[]
        new_dict[value].append(key)
        # print(new_dict)
        
    
    return new_dict


dicta = {"a":10, "b":20, "c":10, "d":20} 
result = dict_change(dicta)
print(result)
