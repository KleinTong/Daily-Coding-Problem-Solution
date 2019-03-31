class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def display(self):
        def helper(item):
            if not item:
                return
            helper(item.left)
            helper(item.right)
            print(item.data, end=' ')


        helper(self)
        print()


def post_order(trace):
    def helper(rest):
        if not rest:
            return None

        flag = rest[-1]
        left_arr = []
        right_arr = []
        for item in rest:
            if item < flag:
                left_arr.append(item)
            elif item > flag:
                right_arr.append(item)

        node = Node(flag)
        node.left = helper(left_arr)
        node.right = helper(right_arr)
        return node


    return helper(trace)


if __name__ == '__main__':
    arr = [2, 4, 3, 8, 7, 5]
    node = post_order(arr)
    print(node)
    node.display()
