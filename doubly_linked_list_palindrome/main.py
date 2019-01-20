from data.doublyLinkedList import DoublyLinkedList, DoublyLinkedNode


def check_palindrome_by_doublylinkedlist(root):
    def left_right(root):
        s = ''
        node = root.headNode().next
        while node.next:
            s += node.data
            node = node.next
        s += node.data
        return s, node


    def right_left(item):
        s = ''
        node = item
        while node.prev:
            s += node.data
            node = node.prev
        return s


    s_left, right_root = left_right(root)
    s_right = right_left(right_root)
    return s_left == s_right


if __name__ == '__main__':
    l = DoublyLinkedList()
    node_1 = DoublyLinkedNode('1')
    node_2 = DoublyLinkedNode('2')
    node_3 = DoublyLinkedNode('1')
    l.insert(node_1)
    l.insert(node_2)
    l.insert(node_3)
    # l.show()

    print(check_palindrome_by_doublylinkedlist(l))
