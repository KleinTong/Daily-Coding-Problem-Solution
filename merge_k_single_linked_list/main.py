class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def __gt__(self, other):
        return self.data > other.data


    def __lt__(self, other):
        return self.data < other.data


    def __eq__(self, other):
        return self.data == other.data


def merge_linked_list(list_a, list_b):
    def helper(left, right):
        if not left:
            return right
        if not right:
            return left

        result = None
        pre_node = None

        if left > right:
            item_a = right
            item_b = left
        else:
            item_a = left
            item_b = right

        result = item_a

        while True:
            if not item_a:
                pre_node.next = item_b
                return result
            if item_a > item_b:
                pre_node.next = helper(item_a, item_b)
                return result
            else:
                pre_node = item_a
                item_a = item_a.next


    return helper(list_a, list_b)


def display_linked_list(root):
    item = root
    while item:
        print(item.data, end=' ')
        item = item.next
    print()


if __name__ == '__main__':
    node_1 = Node(7)
    node_2 = Node(7)
    node_3 = Node(9)
    node_4 = Node(16)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_5 = Node(3)
    node_6 = Node(5)
    node_7 = Node(8)
    node_8 = Node(20)
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8

    list_1 = node_1
    list_2 = node_5

    display_linked_list(list_1)
    display_linked_list(list_2)

    list_3 = merge_linked_list(list_1, list_2)
    display_linked_list(list_3)
