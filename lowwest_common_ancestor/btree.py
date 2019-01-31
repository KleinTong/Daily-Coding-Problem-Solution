from node import Node


class BTree:
    def __init__(self):
        self.root = None
        self.cnt = 0


    def insert(self, node):
        def helper(item, node):
            if not item:
                self.cnt += 1
                return node
            if item.data > node.data:
                item.left = helper(item.left, node)
                item.left.parent = item
            elif item.data < node.data:
                item.right = helper(item.right, node)
                item.right.parent = item
            return item


        self.root = helper(self.root, node)


    def show(self):
        def helper(node):
            if not node:
                return
            print(node.data)
            helper(node.left)
            helper(node.right)


        helper(self.root)


if __name__ == '__main__':
    tree = BTree()
    node_1 = Node(50)
    node_2 = Node(102)
    node_3 = Node(40)
    tree.insert(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.show()
