arr = [5,0,1,3,0,12]

def zero_at_end(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i]!= 0:
            print(arr[i])
            print(arr[j])
            # arr[j] = arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            j = j +1
            print(j)
            print(arr)
zero_at_end(arr)
