#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if (a[j] > a[j+1]):
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
            count+=1

    if(count==0):
        break

print("Array is sorted in",count,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])