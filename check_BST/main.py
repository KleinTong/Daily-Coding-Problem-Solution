def check_BST(root):
    def helper(node):
        if not node:
            return True
        data = node.data
        if node.left:
            if node.left.data > data:
                return False
        if node.right:
            if node.right.data < data:
                return False
        l = helper(node.left)
        r = helper(node.right)
        return l and r


    return helper(root)
