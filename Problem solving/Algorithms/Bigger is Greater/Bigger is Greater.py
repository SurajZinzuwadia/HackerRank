#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
# Complete the biggerIsGreater function below.
def biggerIsGreater(nums): # nums = 'dkhc'
    nums = list(nums) # convert to list ['d','k',...]
    found = False # flag
    i = len(nums) - 2 # counting start from last, cz we have to find next permutation
    # i = 2
    while i >= 0:
        # nums[2] = h < nums[3] = c which is false
        if nums[i] < nums[i + 1]:
           # end at nums[0] = d < nums[1] = k
            found = True
            break
        i -= 1
    if not found:
        return ("no answer")
    else:
        # found that i = 0 , nums , d
        m = findMaxIndex( nums, nums[i]) # m as 2
        nums[i], nums[m] = nums[m], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1] # c,d,k
    return (''.join((nums)))



def findMaxIndex( a, curr):
    ans = -1
    index = 0
    for i in range(index, len(a)):
        if a[i] > curr:
            if ans == -1:
                ans = curr
                index = i
            else:
                ans = min(ans, a[i])
                index = i
    return index
if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)
