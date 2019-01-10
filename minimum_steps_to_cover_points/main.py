def minimum_steps(arr):
    def helper(pos_1, pos_2):
        level_distance = abs(pos_1[0] - pos_2[0])
        verticle_distance = abs(pos_1[1] - pos_2[1])
        return level_distance if level_distance >= verticle_distance else verticle_distance


    result = 0
    for i in range(len(arr) - 1):
        result += helper(arr[i], arr[i+1])

    return result


if __name__ == '__main__':
    arr_1 = [(0, 0), (1, 1), (1, 2)]
    arr_2 = [(0, 0), (2, 2), (1, 2)]
    print(minimum_steps(arr_1))
    print(minimum_steps(arr_2))
