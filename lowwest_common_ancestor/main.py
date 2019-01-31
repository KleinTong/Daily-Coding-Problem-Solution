from btree import BTree
from node import Node


def lca(node_1, node_2):
    def find_parents(node):
        parents = []
        item = node
        while item:
            parents.append(item)
            item = item.parent
        return parents


    node_1_parents = find_parents(node_1)
    item = node_2
    while item:
        if item in node_1_parents:
            return item
        item = item.parent
    return None


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_4 = Node(200)
    node_5 = Node(90)
    node_6 = Node(80)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.insert(node_5)
    tree.insert(node_6)
    # tree.show()
    print(lca(node_4, node_6))
