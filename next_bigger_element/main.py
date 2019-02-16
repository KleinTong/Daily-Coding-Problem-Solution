from node_with_parent import Node
from binary_tree import BTree

def next_bigger(node):
    def mininum_node(node):
        if not node:
            return None
        item = node
        while True:
            if item.left:
                item = item.left
            else:
                return item


    item = node
    if item.right:
        return mininum_node(item.right).data
    else:
        parent = item.parent
        if parent:
            # left subtree
            if parent.left == item:
                return parent.data
            # right subtree
            elif parent.right == item:
                return None
        else:
            return mininum_node(item.right).data


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(10)
    node_2 = Node(5)
    node_3 = Node(30)
    node_4 = Node(22)
    node_5 = Node(35)
    tree.insert_with_parent_setting(node_1)
    tree.insert_with_parent_setting(node_2)
    tree.insert_with_parent_setting(node_3)
    tree.insert_with_parent_setting(node_4)
    tree.insert_with_parent_setting(node_5)
    tree.show()

    print('{}\'s next bigger data is {}'.format(node_1.data, next_bigger(node_1)))
    print('{}\'s next bigger data is {}'.format(node_2.data, next_bigger(node_2)))
