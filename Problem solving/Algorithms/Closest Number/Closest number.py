#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    result = []
    minValue = arr[1] - arr[0]
    for i in range(0,len(arr)-1):
        if(arr[i+1]-arr[i] < minValue):
            minValue = arr[i+1] - arr[i]
    for i in range(0,len(arr)-1):
        if(arr[i+1] - arr[i] == minValue):
            result.append(arr[i])
            result.append((arr[i+1]))
    return result
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(' '.join(map(str, result)))
