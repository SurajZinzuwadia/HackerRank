#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


def printNode(head):
    temp = head
    while (temp != None):
        print(temp.data)
        temp = temp.next

def deleteNode(head, position):
    prev_node = None
    node = head
    if position == 0:
        head = node.next
        return head

    while node is not None:
        for _ in range(position):
            if node.next is not None:
                prev_node = node
                node = node.next
        prev_node.next = node.next
        return head
if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    printNode(llist1)