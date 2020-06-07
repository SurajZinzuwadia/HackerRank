# Solve 5 testcases , rest of another shows runtime error
#!/bin/python3

import os
import sys

#
# Complete the ashtonString function below.
#
def ashtonString(s, k):
    n = len(s)

    # Creating an array to store substrings
    # sub_count = (n * (n + 1)) // 2
    # arr = [0] * sub_count
    #
    # # finding all substrings of string
    # index = 0
    # for i in range(n):
    #     for j in range(1, n - i + 1):
    #         if (s[i:i+j]  not in arr):
    #             arr[index] = s[i:i + j]
    #             index += 1
    #         else:
    #             sub_count-=1
    #             arr.pop(sub_count)
    #
    # arr.sort()

    # Concatenating all substrings
    # res = ""
    # for i in range(sub_count):
    #     res += arr[i]
    #
    # return (res[k-1])
    j=1
    a = set()
    while True:
        for i in range(len(s) - j + 1):
            a.add(s[i:i + j])
        if j == len(s):
            break
        j += 1
        print(list(a))
    a = ''.join(sorted(list(a)))
    return (a[k-1])
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        k = int(input())

        res = ashtonString(s, k)
        print(res)

