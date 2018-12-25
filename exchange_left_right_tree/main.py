from queue import Queue


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.num = 0


    def insert(self, node):
        def helper(item, node):
            if not item:
                self.num += 1
                return node
            if item > node:
                item.left = helper(item.left, node)
            elif item < node:
                item.right = helper(item.right, node)
            else:
                return item
            return item

        self.root = helper(self.root, node)


    def level_display(self):
        q1 = Queue()
        q2 = Queue()
        q1.put(self.root)
        q2.put(self.root)
        while not q2.empty():
            node = q2.get()
            if node.left:
                q1.put(node.left)
                q2.put(node.left)
            if node.right:
                q1.put(node.right)
                q2.put(node.right)
        while not q1.empty():
            print(q1.get(), end=' ')


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __str__(self):
        return str(self.data)


def exch(root):
    def helper(node):
        if not node:
            return
        term = node.left
        node.left = node.right
        node.right = term
        helper(node.right)
        helper(node.left)

    helper(root)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(Node(20))
    tree.insert(Node(10))
    tree.insert(Node(39))
    tree.insert(Node(50))
    # tree.level_display()

    exch(tree.root)
    tree.level_display()
