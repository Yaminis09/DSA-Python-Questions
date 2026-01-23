from os import *
from sys import *
from collections import *
from math import *

def pancakeSort(arr, n):
    # n = len(arr)
    # print("Start:", arr)

    for ni in range(n, 1, -1):

        # reset max index for this pass
        num = 0
        for i in range(ni):
            if arr[i] > arr[num]:
                num = i

        # flip 1: bring max to front
        i = 0
        j = num
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        # flip 2: move max to correct position
        i = 0
        j = ni - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        # print(f"After placing {ni}:", arr)

    # print("Sorted:", arr)
