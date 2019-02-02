from binary_tree import BTree
from node import Node


def level_split(root):
    def helper(node, level):
        if not node:
            return
        if level not in level_dict:
            level_dict[level] = [node]
        else:
            level_dict[level].append(node)
        helper(node.left, level+1)
        helper(node.right, level+1)


    level_dict = {}
    helper(root, 0)
    final_result = float('inf')
    level = None
    for value in level_dict.values():
        result = 0
        for node in value:
            result += node.data
        if final_result > result:
            final_result = result
            level = value
    print(final_result)
    return value


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_4 = Node(1)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.show()
    print(level_split(tree.root))
