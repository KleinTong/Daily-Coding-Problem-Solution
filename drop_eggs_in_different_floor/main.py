def which_floor(eggs, floors):
    def helper(rest_eggs, rest_floors):
        if rest_eggs == 1:
            return rest_floors
        return helper(rest_eggs - 1, rest_floors // 2) + 1


    return helper(eggs, floors)


if __name__ == '__main__':
    print(which_floor(1, 5))
    print(which_floor(2, 5))
    print(which_floor(4, 500))
