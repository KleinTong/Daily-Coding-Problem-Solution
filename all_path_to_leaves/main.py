from datastructure.binary_tree import BTree
from datastructure.node import Node


def all_path(root):
    def helper(node, trace):
        nonlocal result
        if not node:
            return
        if not node.left and not node.right:
            result.append(trace + [node.data])
            return
        helper(node.left, trace + [node.data])
        helper(node.right, trace + [node.data])


    result = []
    helper(root, [])
    return result


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_4 = Node(1000)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.show()
    print(all_path(tree.root))
