#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    n = len(arr)
    Count = '0'
    for i in range(n):
        if i < n//2:
            arr[i][1] = '-'
        if arr[i][0] > Count:
            Count = arr[i][0]
    result = [''] * (int(Count) + 1)
    for i in range(n):
        result[int(arr[i][0])] += arr[i][1] + ' '
    print(''.join(result))


    # L = len(arr)
    # Max = '0'
    # for i in range(L):
    #     if i<L//2:
    #         arr[i][1] = '-'
    #     if arr[i][0]>Max:
    #         Max = arr[i][0]
    # List = ['' for i in range(int(Max) + 1)]
    # for i in range(L):
    #     List[int(arr[i][0])] += arr[i][1]+' '
    #     print(List)
    # print(''.join(List))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
    # print(arr)