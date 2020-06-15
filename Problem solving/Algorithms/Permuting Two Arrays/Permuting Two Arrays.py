#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(0,len(A)):
        if(A[i] + B[i] >= k):
            continue
        else:
            return "NO"
    return "YES"
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)
        print(result)
