def dye(matrix, m, n, target):
    def is_outbound(i, j):
        if i < 0 or i >= len(matrix):
            return True
        if j < 0 or j >= len(matrix[0]):
            return True
        return False


    def helper(marked, i, j, aim):
        if is_outbound(i, j):
            return
        if marked[i][j]:
            return
        marked[i][j] = True
        if matrix[i][j] != aim:
            return
        else:
            matrix[i][j] = target
        helper(marked, i+1, j, aim)
        helper(marked, i-1, j, aim)
        helper(marked, i, j+1, aim)
        helper(marked, i, j-1, aim)


    marked = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    helper(marked, m, n, matrix[m][n])
    return matrix


def display(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    matrix = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']
    ]
    dye(matrix, 1, 1, 'G')
    display(matrix)
