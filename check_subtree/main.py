from binary_tree import BTree
from node import Node


def check_subtree(s, t):
    def eq_trees(tree_1, tree_2):
        if not tree_1:
            if not tree_2:
                return True
            if tree_2:
                return False
        if tree_1.data != tree_2.data:
            return False
        return eq_trees(tree_1.left, tree_2.left) or eq_trees(tree_1.right, tree_2.right)


    def helper(s_root, t_root):
        if eq_trees(s_root, t_root):
            return s_root
        else:
            if s_root.left:
                left = helper(s_root.left, t_root)
                if left:
                    return left
            if s_root.right:
                right = helper(s_root.right, t_root)
                if right:
                    return right
        return None


    return helper(s.root_value(), t.root_value())


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    node_5 = Node(120)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_5)
    tree.show()
    tree_1 = BTree()
    node_4 = Node(102)
    node_6 = Node(120)
    tree_1.insert(node_4)
    tree_1.insert(node_6)
    print(check_subtree(tree, tree_1))
