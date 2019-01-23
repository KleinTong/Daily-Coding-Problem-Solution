class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedNode('head')
        self.cnt = 0
        self.front = self.head


    def insert(self, node):
        self.front.insert(node)
        self.front = node
        self.cnt += 1


    def headNode(self):
        return self.head


    def show(self):
        node = self.head.next
        while node:
            print(node.data, end=' ')
            node = node.next


class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


    def insert(self, node):
        self.next = node
        node.prev = self


if __name__ == '__main__':
    l = DoublyLinkedList()
    node_1 = DoublyLinkedNode(1)
    node_2 = DoublyLinkedNode(2)
    node_3 = DoublyLinkedNode(3)
    l.insert(node_1)
    l.insert(node_2)
    l.insert(node_3)
    l.show()
