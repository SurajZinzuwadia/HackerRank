#!/bin/python3

import os
import sys
import itertools
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    res = list(itertools.product(keyboards, drives))
    n = len(res)
    temp = []
    for i in range(n):
        temp.append(res[i][0] + res[i][1])
    temp.append(-1)
    return (max([x for x in temp if x <= b]))

# sums = []
# for t in list(product(kbds, usbs)):
#     sums.append(t[0] + t[1])
# sums.append(-1)
# print(max([x for x in sums if x <= s]))

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
