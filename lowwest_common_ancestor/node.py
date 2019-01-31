class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


    def __str__(self):
        return 'this node\'s data is ' + str(self.data)
