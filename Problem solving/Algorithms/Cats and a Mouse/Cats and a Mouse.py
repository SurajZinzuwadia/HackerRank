#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if (abs(x-z) > abs(y - z) ):
        print("Cat B")
    elif(abs(x - z) < abs(y - z)):
        print("Cat A")
    else:
        print("Mouse C")
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        # x for cat A
        x = int(xyz[0])
        # y for cat B
        y = int(xyz[1])
        #z for mouse C
        z = int(xyz[2])

        result = catAndMouse(x, y, z)

