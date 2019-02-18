def largest_rectangle(matrix):
    def spread_down(left, right, i):
        if i >= height:
            return 0
        for j in range(left, right+1):
            if matrix[i][j] == 0:
                return 0
        return right - left + 1 + spread_down(left, right, i + 1)


    width = len(matrix[0])
    height = len(matrix)
    max_cnt = 0
    left = -1
    result = 0
    for i in range(height):
        left = -1
        for j in range(width):
            result = 0
            if matrix[i][j] == 0:
                left = -1
            else:
                if left == -1:
                    left = j
                next_line = spread_down(left, j, i)
                result += next_line
                max_cnt = max(max_cnt, result)
    return max_cnt


if __name__ == '__main__':
    matrix = [
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]
    ]
    print(largest_rectangle(matrix))
