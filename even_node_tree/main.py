from node import Node


def isTreeEven(root):
    def helper(item):
        if not item:
            return 0
        else:
            cnt = 1
            for child_node in item.iterate_children():
                cnt += helper(child_node)
            return cnt


    return True if helper(root) % 2 == 0 else False


def how_many_edges_to_remove(root):
    def helper(item):
        cnt = 0
        for child in item.iterate_children():
            if isTreeEven(child):
                print(str(item) + ' => ' + str(child))
                cnt += 1
            cnt += helper(child)
        return cnt

    
    return helper(root)


if __name__ == '__main__':
    root = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)

    left = Node(11)
    right = Node(22)

    root.append_child(two, three)
    three.append_child(four, five)
    four.append_child(six, seven, eight)

    five.append_child(left)
    left.append_child(right)

    print(how_many_edges_to_remove(root))
