#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    count = 0
    temp = []
    for i in arr:
        if (i not in temp):
            x = arr.count(i)
            if(x%2 == 0):
                x = x /2
                count+=x
            else:
                x-=1
                x = x/2
                count += x
            temp.append(i)
    return int(count)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, arr)
    print(result)
