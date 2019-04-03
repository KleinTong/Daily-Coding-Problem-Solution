def rotate_90(matrix):
    result = []

    for j in range(len(matrix[0])):
        part = []
        for i in range(len(matrix) - 1, -1, -1):
            part.append(matrix[i][j])
        result.append(part)

    return result


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(rotate_90(matrix))

    matrix = [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [7, 8, 9, 10],
        [4, 5, 6, 7]
    ]
    print(rotate_90(matrix))
