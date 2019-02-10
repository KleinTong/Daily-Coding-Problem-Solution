class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def make_list(num):
    is_negative = False
    head = None
    tail = None
    cnt = 0
    if num < 0:
        is_negative = True
        num = -num
    while num > 0:
        digit = num % 10
        num = num // 10
        if is_negative:
            item = Node(-digit)
        else:
            item = Node(digit)
        if cnt == 0:
            head = item
            tail = item
        else:
            tail.next = item
            tail = item
        cnt += 1
    return head


def get_num(node):
    if not node:
        return 0
    up = get_num(node.next)
    return node.data + up * 10


def integer_sum(node_1, node_2):
    ans = get_num(node_1) + get_num(node_2)
    print('num_1 is', get_num(node_1))
    print('num_2 is', get_num(node_2))
    node = make_list(ans)
    return node


if __name__ == '__main__':
    node_1 = make_list(1000)
    node_2 = make_list(-30)
    node = integer_sum(node_1, node_2)
    print(get_num(node))
