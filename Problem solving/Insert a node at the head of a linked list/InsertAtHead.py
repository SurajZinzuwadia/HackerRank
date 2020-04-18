
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def printNode(head):
        temp = head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

def insertNodeAtHead(head, data):
	node = SinglyLinkedListNode(data)
    if head:
        node.next = head
        head = node
    else:
        head = node
    return head

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
        print(llist.head.data)
    printNode(llist.head)

