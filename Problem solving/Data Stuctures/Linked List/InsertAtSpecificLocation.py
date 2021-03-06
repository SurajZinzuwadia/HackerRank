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


def insertNodeAtPosition(head, data, position):
    prev_node = head
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        return new_node
    while prev_node is not None:
        new_node = SinglyLinkedListNode(data)

        for _ in range(position-1):
            if prev_node.next is not None:
                prev_node = prev_node.next
        new_node.next = prev_node.next
        prev_node.next = new_node
        return head


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    printNode(llist_head)