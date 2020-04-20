class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAfter(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
        self.last = node


    def print(self):
            temp = self.head
            while(temp!=None):
                print(temp.data)
                temp = temp.next


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insertAfter(llist_item)

    llist.print()
