# 思路， 你要找出在一棵树之中重量最大的那条路径
# 你有什么想法？
# 一颗树的最大路径有三种情况，第一种是左子树，第二种是右子树，第三种是跨越子树根结点。
# 如果是第三种情况的话，它必然会到一个叶节点

pool = {'ab': 3, 'ac': 5, 'ad': 8, 'de': 2, 'df': 4, 'eg': 1, 'eh': 1}


class Tree:
    def __init__(self, pool):
        self.edge_pool = pool


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


    def insert_left(self, item):
        self.left = item


    def insert_right(self, item):
        self.right = item


def weight(tree):
    def drill(item):
        if not item:
            return 0, ''
        left_result, left_path = drill(item.left)
        left_result += check_weight(item, item.left)
        right_result, right_path = drill(item.right)
        right_result += check_weight(item, item.right)
        if left_result > right_result:
            return left_result, left_path + item.name
        else:
            return right_result, item.name + right_path


    def helper(item):
        if not item:
            return 0, ''
        left_result, left_path = drill(item.left)
        left_result += check_weight(item, item.left)
        right_result, right_path = drill(item.right)
        right_result += check_weight(item, item.right)
        final_result = left_result + right_result
        final_path = left_path + item.name + right_path
        return final_result, final_path


    return helper(tree)


# def weight(tree):
#     def helper(item):
#         if not item:
#             return 0, ''
#
#         left_result, left_path, left_cross_result, left_cross_path = helper(item.left)
#         left_result += check_weight(item, item.left)
#         right_result, right_path, right_cross_result, right_cross_path = helper(item.right)
#         right_result += check_weight(item, item.right)
#
#         cross_result, cross_path = cross_path(item)
#         # 0 means stopping here
#         if left_result > right_result and left_result > cross_result:
#             return left_result, left_path + item.name
#         elif right_result > left_result and right_result > cross_result:
#             return right_result, item.name + right_path
#         return max(left_result, right_result, cross_result, 0)
#
#
#     return helper(tree)


# def cross_path(node):
#     def helper(item):
#         if not item:
#             return 0, ''
#         left_result, left_path = helper(item.left)
#         left_result += check_weight(item, item.left)
#         right_result, right_path = helper(item.right)
#         right_result += check_weight(item, item.right)
#         final_result = left_result + right_result
#         final_path = left_path + item.name + right_path
#         # 0 means stopping here
#         if final_result > 0:
#             return final_result, final_path
#         return 0, ''
#
#
#     return helper(node)


def check_weight(parent, child):
    if not child:
        return 0
    return pool[parent.name + child.name]


if __name__ == '__main__':
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_f = Node('f')
    node_g = Node('g')
    node_h = Node('h')

    node_a.insert_left(node_b)
    node_a.insert_right(node_d)
    node_d.insert_left(node_e)
    node_d.insert_right(node_f)
    node_e.insert_left(node_g)
    node_e.insert_right(node_h)

    print(weight(node_a))
