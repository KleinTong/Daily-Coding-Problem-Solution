def clockwise(arr, m, n):
    w = min(m, n)


    def tube(level):
        if w - 2 * level <= 0:
            return

        left = level
        right = n - 1 - level
        up = level
        down = m - 1 - level

        if left >= right:
            col_print(n-1-level, level, down)
            return
        elif up >= down:
            row_print(level, left, right)
            return

        if level <= n-1-level:
            row_print(level, level, n-1-level)
        if level + 1 <= m-2-level:
            col_print(n-1-level, level+1, m-2-level)
        if n - 1 - level >= level:
            row_print(m-1-level, n-1-level, level)
        if m - 2 - level >= 1 + level:
            col_print(level, m-2-level, 1 + level)
        tube(level + 1)


    def row_print(row, a, b):
        if a < b:
            for j in range(a, b + 1):
                print(arr[row][j])
        else:
            for j in range(a, b - 1, -1):
                print(arr[row][j])


    def col_print(col, a, b):
        if a < b:
            for i in range(a, b + 1):
                print(arr[i][col])
        else:
            for i in range(a, b - 1, -1):
                print(arr[i][col])


    tube(0)


if __name__ == '__main__':
    arr1 = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

    arr2 = [[1, 2],
            [3, 4],
            [5, 6]]

    arr3 = [[1]]

    arr4 = []

    # clockwise(arr1, 4, 5)
    clockwise(arr2, 3, 2)
    # clockwise(arr3, 1, 1)
    # clockwise(arr3, 0, 1)
