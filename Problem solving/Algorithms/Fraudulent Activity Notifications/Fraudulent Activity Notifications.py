#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
from collections import deque


def median(v, d):
    count = 0
    if d%2==0:
        m1 = None
        m2 = None
        for i in range(len(v)):
            count += v[i]
            if count >= d/2 and m1 is None:
                m1 = i
            if count >= d/2 + 1:
                m2 = i
                break
        return (m1 + m2)/2
    else:
        for i in range(len(v)):
            count += v[i]
            print("Vi",v[i])
            print("Count:", count)
            if count > d/2:
                return i

    return -1

def activityNotifications(expenditure, d):
    dq = deque(expenditure[: d])
    print(dq)
    v = [0]*201
    for n in dq:
        v[n] += 1
    print(v)
    count = 0
    for current in expenditure[d:]:
        if current >= median(v, d)*2:
            count += 1
        v[current] += 1
        dq.append(current)
        v[dq.popleft()] -= 1
    return count

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
