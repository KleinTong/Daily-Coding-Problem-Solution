def solver(matrix, target):
    size = len(matrix)


    def is_out_of_bounds(i, j):
        if i < 0 or i > size - 1:
            return True
        if j < 0 or j > size - 1:
            return True

        return False


    def helper(i, j, rest):
        if not rest:
            return True
        if is_out_of_bounds(i, j):
            return False
        if matrix[i][j] == rest[0]:
            return helper(i + 1, j, rest[1:]) or helper(i, j + 1, rest[1:])
        else:
            return False


    for i in range(size):
        for j in range(size):
            if helper(i, j, target):
                return True
    return False


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
             ['O', 'B', 'Q', 'P'],
             ['A', 'N', 'O', 'B'],
             ['M', 'A', 'S', 'S']]
    print(solver(matrix, 'FOAM'))
    print(solver(matrix, 'FOAN'))
    print(solver(matrix, 'FABQ'))
    print(solver(matrix, 'FACI'))
    print(solver(matrix, 'FABQOB'))
    print(solver(matrix, 'FABQOBP'))
    print(solver(matrix, 'FABQOBS'))
    print(solver(matrix, 'MASS'))
