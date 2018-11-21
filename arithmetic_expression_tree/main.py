from operator import add, sub, truediv, mul


def parser(tree):
    op_dict = {'+': add, '-': sub, '*': mul, '/': truediv}

    def helper(node):
        if not node:
            return 0

        if node.data in op_dict:
            return op_dict[node.data](helper(node.left), helper(node.right))
        elif float(node.data) >= 0 and float(node.data) <= 9:
            return float(node.data)
        else:
            raise ValueError()


    result = helper(tree)
    print(result)
    return result


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def append_left(self, node):
        self.left = node


    def append_right(self, node):
        self.right = node


if __name__ == '__main__':
    root = Node('*')
    node_l = Node('+')
    node_r = Node('+')
    node_l_1 = Node('3')
    node_l_2 = Node('2')
    node_r_1 = Node('4')
    node_r_2 = Node('5')

    node_l.append_left(node_l_1)
    node_l.append_right(node_l_2)

    node_r.append_left(node_r_1)
    node_r.append_right(node_r_2)

    root.append_left(node_l)
    root.append_right(node_r)

    parser(root)
