arr = [3, 7, 2, 9]

def two_max_element_sum(arr):
    max_element = arr[0]
    second_max_element = float('-inf')
    # second_max_element = arr[0]
    for i in range(len(arr)):

        if arr[i]>max_element:
            second_max_element = max_element
            max_element = arr[i]
        elif arr[i]> second_max_element and arr[i] != max_element:
            second_max_element = arr[i]
    final_sum = max_element + second_max_element
    print(f"final sum {final_sum}")
    
two_max_element_sum(arr)
    
