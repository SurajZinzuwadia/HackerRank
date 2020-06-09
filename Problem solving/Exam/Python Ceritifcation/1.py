#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
from statistics import mean
def avg(*nums):
    x = list(nums)
    temp = sum(nums)/len(nums)
    return (temp)

if __name__ == '__main__':

    nums = list(map(int, input().split()))
    res = avg(*nums)
    print(res)
