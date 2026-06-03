

"""
Input:
"aabbcde"
Output:
"c"
"""
# sort the array
# count the element
def first_non_repeating_character(stra):
    stra= stra.lower()
    char_counts = {}
    for char in stra:
        if char in char_counts.keys():
            
            char_counts[char] = char_counts[char]+1
        else:
            char_counts[char] = 1
    print(char_counts)
    
    for i,j in char_counts.items():
        if j == 1:
          return i
    
    
stra= "yaminisingh"
results = first_non_repeating_character(stra)
print(results)
