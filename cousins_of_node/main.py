from binary_tree import BTree
from node import Node


def find_cousins(root, node):
    def get_level(root, node):
        def worker(item, level_cnt):
            if item == node:
                return level_cnt
            if not item:
                return -1
            return max(worker(item.left, level_cnt + 1), worker(item.right, level_cnt + 1))


        return worker(root, 1)


    def helper(item, current_level, target_level):
        if not item:
            return []
        if current_level == target_level:
            return [item]
        elif current_level > target_level:
            return []
        return helper(item.left, current_level + 1, target_level) + \
                helper(item.right, current_level + 1, target_level)


    node_level = get_level(root, node)
    return helper(root, 1, node_level)


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(130)
    node_3 = Node(40)
    node_4 = Node(152)
    node_5 = Node(102)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.insert(node_5)
    cousins = find_cousins(tree.root, node_5)
    for cousin in cousins:
        print(cousin)
