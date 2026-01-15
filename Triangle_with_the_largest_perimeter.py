"""https://www.naukri.com/code360/problems/triangle-with-the-largest-perimeter_1463974?kunjiRedirection=true"""

from os import *
from sys import *
from collections import *
from math import *

def maxPerimeterTriangle(arr,  n):
    # Sort the array
    arr.sort()

    for i in range(n-1,1,-1):
        
        a = arr[i-2]
        b = arr[i-1]
        c = arr[i]

        if a+b >c:
            return a+b+c

    return 0




