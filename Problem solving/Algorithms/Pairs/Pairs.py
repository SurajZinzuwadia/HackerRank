#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    numbers = set()
    count = 0
    for n in arr:
        if n + k in numbers:
            count += 1
        if n - k in numbers:
            count += 1
        numbers.add(n)
    return count



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print(result)
