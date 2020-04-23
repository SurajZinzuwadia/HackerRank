#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank.append(n+1-index)
        print(rank)
    return rank

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
