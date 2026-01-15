"""
You are given two arrays of the same size. Your task is to maximize the possible sum that can be calculated using elements of the two given arrays. You are allowed to swap elements between the arrays at the same position any number of times to achieve this.
"""

from os import *
from sys import *
from collections import *
from math import *

def calculateMaximisedSum(arr1, arr2, N):
    keep = abs(arr1[0] - arr2[0])
    swap = abs(arr2[0] - arr1[0])

    for i in range(1, N):
        a, b = arr1[i], arr2[i]
        pa, pb = arr1[i-1], arr2[i-1]

        # no swap at i
        new_keep = max(
            keep + abs(a - b) + abs(a - pb),
            swap + abs(a - b) + abs(a - pa)
        )

        # swap at i
        new_swap = max(
            keep + abs(b - a) + abs(b - pb),
            swap + abs(b - a) + abs(b - pa)
        )

        keep, swap = new_keep, new_swap

    return max(keep, swap)
    
    

    
