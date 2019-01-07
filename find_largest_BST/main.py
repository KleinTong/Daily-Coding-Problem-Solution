class Sub_tree:
    def __init__(self, node, size, bool):
        self.node = node
        self.size = size
        self.bool = bool


    def merge(self, other, node=None):
        if self.bool and other.bool and node:
            self.node = node
            self.size = self.size + other.size + 1
        else:
            self.bool = False
            other.bool = False
            if self.size < other.size:
                self.node = other.node
                self.size = other.size


    def __eq__(self, other):
        return self.size == other.size


    def __gt__(self, other):
        return self.size > other.size


    def __lt__(self, other):
        return self.size < other.size


    def __str__(self):
        return 'data is ' + str(self.node) + '; size is ' + str(self.size)


def largest_sub_BST(root):
    def helper(node):
        left_sub_tree = Sub_tree(None, 0, True)
        right_sub_tree = Sub_tree(None, 0, True)
        result_root = True
        if not node.left and not node.right:
            return Sub_tree(node, 1, True)
        if node.left:
            if node.left.data > node.data:
                result_root = False
            left_sub_tree = helper(node.left)
        if node.right:
            if node.right.data < node.data:
                result_root = False
            right_sub_tree = helper(node.right)
        if result_root:
            left_sub_tree.merge(right_sub_tree, node)
            return left_sub_tree
        else:
            left_sub_tree.merge(right_sub_tree)
            return left_sub_tree


    return helper(root)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert_left(self, other):
        self.left = other


    def insert_right(self, other):
        self.right = other


    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    example_tree = Node(50)
    print('example_tree', example_tree)
    a = Node(20)
    b = Node(30)
    c = Node(60)
    d = Node(10)
    print('a', a)
    print('b', b)
    print('c', c)
    example_tree.insert_right(a)
    example_tree.insert_left(c)
    a.insert_right(b)
    a.insert_left(d)
    print(largest_sub_BST(example_tree))
    print(largest_sub_BST(a))
