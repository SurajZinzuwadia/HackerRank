import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):

        # Base case
        if root is None:
            return
        # Create an empty queue for level order traversal
        q = []

        # Enqueue root and initialize height
        q.append(root)

        while q:

            # nodeCount (queue size) indicates number
            # of nodes at current lelvel.
            count = len(q)

            # Dequeue all nodes of current level and
            # Enqueue all nodes of next level
            while count > 0:
                temp = q.pop(0)
                print(temp.data, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                count -= 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
