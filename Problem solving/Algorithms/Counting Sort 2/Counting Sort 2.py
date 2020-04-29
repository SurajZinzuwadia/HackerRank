#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    countList = [0] * 100
    for i in range(len(arr)):
        countList[arr[i]] += 1
    values = []
    for i in range(len(countList)):
        values += countList[i] * [i]
    return values
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
