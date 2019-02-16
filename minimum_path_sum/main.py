from binary_tree import BTree
from node import Node


def minimum_sum_path(tree):
    def helper(node):
        if not node:
            return 0
        return min(helper(node.left), helper(node.right)) + node.data


    return helper(tree.root)


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_4 = Node(20)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.show()

    print(minimum_sum_path(tree.root))
