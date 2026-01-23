"""
problem - https://www.naukri.com/code360/problems/pancake-sorting_1262344?kunjiRedirection=true
"""

from os import *
from sys import *
from collections import *
from math import *

def pancakeSort(arr, n):
    flips = []

    for ni in range(n, 1, -1):

        # find index of max element
        max_idx = 0
        for i in range(ni):
            if arr[i] > arr[max_idx]:
                max_idx = i

        # if max already at correct position, skip
        if max_idx == ni - 1:
            continue

        # flip max to front
        if max_idx != 0:
            arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            flips.append(max_idx + 1)

        # flip to correct position
        arr[:ni] = reversed(arr[:ni])
        flips.append(ni)

    return flips
