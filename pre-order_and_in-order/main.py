def reverse(pre_order, in_order):
    def make_tree(arr):
        nonlocal pre_index
        if not arr:
            return None
        data = pre_order[pre_index]
        pre_index += 1
        in_index = arr.index(data)
        node = Node(data)
        node.left = make_tree(arr[:in_index])
        node.right = make_tree(arr[in_index+1:])
        return node


    pre_index = 0
    root = make_tree(in_order)
    return root


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


    def show(self):
        def helper_pre(node):
            if not node:
                return
            print(node.data)
            helper_pre(node.left)
            helper_pre(node.right)


        def helper_in(node):
            if not node:
                return
            helper_in(node.left)
            print(node.data)
            helper_in(node.right)

        helper_pre(self.root)
        print()
        helper_in(self.root)


if __name__ == '__main__':
    pre_order = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

    root = reverse(pre_order, in_order)
    tree = Tree(root)
    tree.show()
