#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    count = 0
    temp = []
    for i in A:
        if i in B:
            B.remove(i)
            count+=1
            print(i)
    if count < len(A):
        count +=1
    else:
        count-=1
    print("count",count)
if __name__ == '__main__':

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)
