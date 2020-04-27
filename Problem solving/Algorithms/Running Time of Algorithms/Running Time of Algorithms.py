#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count = 0
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while(temp < arr[j] and j>=0):
            arr[j+1] = arr[j]
            # print(*arr)
            count+=1
            j-=1
        arr[j+1] = temp
        # print(*arr)
    print(count)
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)
