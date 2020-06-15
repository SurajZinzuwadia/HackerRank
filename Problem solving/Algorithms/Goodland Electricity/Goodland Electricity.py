#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    n = len(arr)
    selected = [0] * n
    count = 0
    i = k - 1
    while i < n:
        # reached before
        if selected[i] == 1:
            return -1

        if arr[i] == 1:
            selected[i] = 1
            count += 1
            i += 2 * k - 1
        else:
            i -= 1
    # i goes over
    if i - k + 1 < n:
        if sum(arr[n - k - 1:]) >= 1:
            count += 1
        else:
            return -1
    return count
if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)
    print(result)