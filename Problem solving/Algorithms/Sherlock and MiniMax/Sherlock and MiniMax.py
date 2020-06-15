# Dintdn't passed test case 8,9,10 due to time complexity

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndMinimax function below.

def sherlockAndMinimax(arr, p, q):
    min1=[]
    temp=[]
    arr.sort()
    for i in range(p,q+1):
        for j in arr:
            temp.append(abs(i-j))
        min1.append(min(temp))
        temp=[]
    return (min1.index(max(min1))+p)
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pq = input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)
    print(result)