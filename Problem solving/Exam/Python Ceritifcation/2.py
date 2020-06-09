#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
        self.area()
    def area(self):
        return (float('%.2f'%(self.breadth * self.length)))

class Circle:
    def __init__(self, r):
        self.r = r
        self.area()
    def area(self):
        PI = math.pi
        return (float( '%.2f'%(PI * (self.r * self.r))))


if __name__ == '__main__':
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        print("%.2f\n" % shape.area())
