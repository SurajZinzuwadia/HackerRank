#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr, n):
    d = {}
    i = 0
    while i<n:
        d[arr[i]] = i
        i+=1
    i=0
    print(d)
    while n>0 and k>0:
        if arr[i]<n:
            tmp = d[n]
            arr[d[n]] = arr[i]
            arr[i] = n
            tmp = d[arr[d[n]]]
            d[arr[d[n]]] = d[n]
            d[n] = tmp
            print(d)
            k-=1
        n-=1
        i+=1
    return arr
if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr,n)
    print(result)

