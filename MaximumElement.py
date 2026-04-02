arr = [-3, 7, 2, 9, 4]

def max_element(arr):
    element_max = arr[0] # Don't put 0, as in some hidden case we don't know what numbers are there. Safer to assume first number is the maximum.
    for i in range(len(arr)):
        
        if arr[i]>element_max:
            element_max = arr[i]
    #print(element_max)
    return element_max
