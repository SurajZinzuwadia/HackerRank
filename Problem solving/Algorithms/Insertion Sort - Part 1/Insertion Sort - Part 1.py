#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    for i in range(n-1,0,-1):
        temp = arr[i]
        j = i-1
        while(temp < arr[j] and j>=0):
            arr[j+1] = arr[j]
            print(*arr)
            j-=1
        arr[j+1] = temp
    print(*arr)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
