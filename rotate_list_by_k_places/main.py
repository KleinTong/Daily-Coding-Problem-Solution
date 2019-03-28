class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def rotate(node, k):
    head = node
    item = node
    parent = None
    for i in range(k):
        parent = item
        item = item.next
    new_head = item
    parent.next = None

    item = new_head
    tail = None

    while True:
        if not item.next:
            tail = item
            break
        item = item.next
    tail.next = head

    return new_head


def display(root):
    item = root
    print('{} '.format(item.data), end='')
    item = item.next
    while item:
        print('-> {} '.format(item.data), end='')
        item = item.next
    print()


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    display(node_1)
    item = rotate(node_1, 2)
    display(item)
