# it shows time complexity error as the answers are correct.
# So it is not submitted
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#
from collections import Counter,defaultdict
def stringAnagram(dictionary, query):
    d  = defaultdict(set)
    length2 = len(dictionary)
    length = len(query)
    for i in range(0,length2):
        u = ''.join(sorted(dictionary[i]))
        v = len(dictionary[i])
        # d[u].add(v)
        d[v].add(u)
    print(d)
    for i in range(0,length):
        query[i] = ''.join(sorted(query[i]))
        word_len = len(query[i])
        if word_len in d:
            print(query[i],d[word_len])
            if (query[i] == d[word_len]):
                print("query",query[i])

    # length = len(query)
    # temp = [] * length
    # for i in range(0,length):
    #     word = sorted(query[i])
    #     count = 0
    #     for dic in dictionary:
    #         if word == sorted(dic):
    #             count+=1
    #     temp.insert(i,count)
    #
    # return (temp)
    # print(temp)
    # length = len(query)
    # length2 = len(dictionary)
    # temp = [] * length
    # count = 0
    # for i in range(0,length):
    #     count = 0
    #     for j in range(0,length2):
    #         if (len(query[i]) == len(dictionary[j])):
    #             if (Counter(query[i]) == Counter(dictionary[j])):
    #                 count +=1
    #     temp.insert(i,count)
    # print(temp)
    # temp = [] * length
    # count = 0
    # for i in range(0,length):
    #     count = 0
    #     s1 = sorted(query[i])
    #
    #     for j in range(0,length2):
    #         s2 = sorted(dictionary[j])
    #
    #         if (s1 == s2):
    #
    #             count+=1
    #     temp.insert(i,count)
    # print (temp)
# Write your code here


if __name__ == '__main__':

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)
    print(result)
