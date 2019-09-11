class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


    def append_child(self, *items):
        for item in items:
            self.children.append(item)


    def iterate_children(self):
        for child in self.children:
            yield child


    def __str__(self):
        return str(self.data)
        # return 'data is {}'.format(self.data)


if __name__ == '__main__':
    root = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    root.append_child(one)
    root.append_child(two)
    root.append_child(three)

    for item in root.iterate_children():
        print(item)