from binary_tree import BTree
from node import Node


def deepest_node(root):
    def helper(node, depth):
        if not node.left and not node.right:
            return node, depth
        left_result = None, -1
        right_result = None, -1
        if node.left:
            left_result = helper(node.left, depth + 1)
        if node.right:
            right_result = helper(node.right, depth + 1)
        if left_result[0] and right_result[0]:
            if left_result[1] > right_result[1]:
                return left_result
            else:
                return right_result
        elif left_result[0]:
            return left_result
        elif right_result[0]:
            return right_result


    return helper(root, 0)


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_4 = Node(400)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.show()
    node, depth = deepest_node(tree.root)
    print('deepest node is', node.data)
