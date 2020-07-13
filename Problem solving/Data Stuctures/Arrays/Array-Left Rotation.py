import math
import os
import random
import re
import sys

if __name__ == '__main__':

    testcase = int(input())
    while(testcase):
        nd= input().split()
        n = int(nd[0])
        d = int(nd[1])
        a = list(map(int, input().rstrip().split()))
        print(*(a[d%n:] + a[:d%n]))
        testcase-=1
