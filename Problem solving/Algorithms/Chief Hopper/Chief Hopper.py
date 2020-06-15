#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chiefHopper function below.
def chiefHopper(arr):
    botEnergy = 0
    for height in reversed(arr):
        botEnergy = (height+botEnergy+1)//2
    return botEnergy
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

