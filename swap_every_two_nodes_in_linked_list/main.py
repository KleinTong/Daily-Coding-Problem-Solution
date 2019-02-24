class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap(node):
    def helper(item):
        left_item = item
        right_item = item.next
        if not right_item:
            return left_item
        else:
            aux = right_item.next
            left_item.next = helper(aux)
            right_item.next = left_item
            return right_item


    item = helper(node)
    return item


def show_linked_list(root):
    item = root
    while True:
        if not item:
            break
        print(item.data, end=' ')
        item = item.next
    print()


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    show_linked_list(node_1)
    node = swap(node_1)
    show_linked_list(node)
