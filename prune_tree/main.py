class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert_left(self, node):
        self.left = node


    def insert_right(self, node):
        self.right = node


def display(node):
    def helper(item):
        if not item:
            return
        print(item.data, end=' ')
        helper(item.left)
        helper(item.right)


    helper(node)
    print()


def prune(root):
    def helper(node):
        if not node:
            return None
        node.left = helper(node.left)
        node.right = helper(node.right)
        if not node.left and not node.right:
            if node.data == 1:
                return node
            elif node.data == 0:
                return None
        else:
            return node


    root = helper(root)
    return root


if __name__ == '__main__':
    node_1 = Node(0)
    node_2 = Node(1)
    node_3 = Node(0)
    node_4 = Node(1)
    node_5 = Node(0)
    node_6 = Node(0)
    node_7 = Node(0)

    node_1.insert_left(node_2)
    node_1.insert_right(node_3)
    node_3.insert_left(node_4)
    node_3.insert_right(node_5)
    node_4.insert_left(node_6)
    node_4.insert_right(node_7)

    display(node_1)
    prune(node_1)
    display(node_1)
