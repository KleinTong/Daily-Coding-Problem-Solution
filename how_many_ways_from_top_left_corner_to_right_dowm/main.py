def calculate_ways(matrix):
    cnt = 0
    height = len(matrix)
    width = len(matrix[0])
    def helper(i, j):
        nonlocal cnt
        if i >= height or j >= width:
            return
        if matrix[i][j] == 1:
            return
        if i == height - 1 and j == width - 1:
            cnt += 1
            return
        helper(i + 1, j)
        helper(i, j + 1)


    helper(0, 0)
    return cnt


if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0]
    ]
    print(calculate_ways(matrix))
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0]
    ]
    print(calculate_ways(matrix))
