#!/bin/python3

import math
import os
import random
import re
import sys
import math

def encryption(s):
    s = s.replace(" ", "") # Replcing white spaces
    sr = len(s) ** 0.5  # which is square root
    col = int(sr) if math.ceil(sr) == int(sr) else int(sr)+1 # condition according to question

    word = ''
    for i in range(col):
        p = i
        while p < len(s):
            word = word + s[p]
            p += col
        word = word + ' '

    return word
if __name__ == '__main__':

    s = input()

    result = encryption(s)
    print(result)

