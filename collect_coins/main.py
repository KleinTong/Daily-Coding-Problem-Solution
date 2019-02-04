def collect_coins(matrix):
    def helper(i, j):
        if i >= height:
            return 0
        if j >= width:
            return 0
        coin = matrix[i][j]
        right_choice = helper(i, j+1)
        down_choice = helper(i+1, j)
        my_choice = max(right_choice, down_choice)
        return coin + my_choice


    height = len(matrix)    # i
    width = len(matrix[0])  # j
    return helper(0, 0)


if __name__ == '__main__':
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]
    print(collect_coins(matrix))
