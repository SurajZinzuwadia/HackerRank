#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
from collections import defaultdict
# Complete the jimOrders function below.
def jimOrders(orders):
    serve_time = [] # take serve_time list
    for i, v in enumerate(orders): # use of enumerate
        serve_time.append([v[0] + v[1], i + 1]) # append sum and customer index+1
    serve_time.sort() # sort the server_time list
    order = [x[1] for x in serve_time]
    return order

if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)
    print(result)